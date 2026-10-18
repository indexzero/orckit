#!/usr/bin/env python3
"""Offline checks for fragment composition and kit scaffolding."""

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("compose", ROOT / "create/compose.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CompositionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = self.root / "kit.json"
        self.config = {"documents": {}}

    def write(self, path, text):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(text.encode("utf-8"))
        return file

    def composer(self):
        self.manifest.write_text(json.dumps(self.config))
        return MODULE.Composer(self.manifest)

    def test_convention_needs_no_fragment_registration(self):
        recipe = self.write("review.md", "# Review\n@rules.writing\n")
        self.write("fragments/rules/writing.md", "Plain language.\n")
        self.assertEqual(self.composer().resolve(recipe), "# Review\nPlain language.\n")
        self.write("fragments/rules/writing.md", "Technical English.\n")
        self.assertEqual(self.composer().resolve(recipe), "# Review\nTechnical English.\n")
        self.assertEqual(self.config, {"documents": {}})

    def test_area_and_fragment_name_come_from_the_filesystem(self):
        recipe = self.write("root.md", "@custom_area.new_fragment\n")
        self.write("fragments/custom_area/new_fragment.md", "New content.\n")
        self.assertEqual(self.composer().resolve(recipe), "New content.\n")

    def test_shared_fragment_is_not_a_cycle(self):
        recipe = self.write("root.md", "@left.md\n@right.md\n@shared.md\n")
        self.write("left.md", "Left\n@shared.md\n")
        self.write("right.md", "Right\n@shared.md\n")
        self.write("shared.md", "Shared.\n")
        self.assertEqual(self.composer().resolve(recipe), "Left\nShared.\nRight\nShared.\nShared.\n")

    def test_real_cycle_reports_the_chain(self):
        recipe = self.write("root.md", "@child.md\n")
        self.write("child.md", "@root.md\n")
        with self.assertRaisesRegex(MODULE.CompositionError, "root.md -> child.md -> root.md"):
            self.composer().resolve(recipe)

    def test_nested_fragment_order_and_whitespace(self):
        recipe = self.write("root.md", "Before\n@charter.context\nAfter\n")
        self.write("fragments/charter/context.md", "@charter.first\n@charter.second\n")
        self.write("fragments/charter/first.md", "\nFirst.\n\n")
        self.write("fragments/charter/second.md", "Second.")
        self.assertEqual(self.composer().resolve(recipe), "Before\n\nFirst.\n\nSecond.\nAfter\n")

    def test_missing_conventional_fragment_has_source_location(self):
        recipe = self.write("root.md", "Title\n@rules.missing\n")
        with self.assertRaisesRegex(MODULE.CompositionError, r"root.md:2: Missing fragment"):
            self.composer().resolve(recipe)

    def test_missing_fragment_fails(self):
        recipe = self.write("root.md", "@missing.md\n")
        with self.assertRaisesRegex(MODULE.CompositionError, "Missing fragment"):
            self.composer().resolve(recipe)

    def test_duplicate_manifest_key_fails(self):
        self.manifest.write_text('{"documents": {}, "documents": {}}')
        with self.assertRaisesRegex(MODULE.CompositionError, "Duplicate manifest key"):
            MODULE.Composer(self.manifest)

    def test_parent_escape_and_absolute_paths_fail(self):
        for reference in ("../outside.md", "/outside.md"):
            with self.subTest(reference=reference):
                recipe = self.write("root.md", "@" + reference + "\n")
                with self.assertRaises(MODULE.CompositionError):
                    self.composer().resolve(recipe)

    def test_symlink_escape_fails(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "outside.md"
            target.write_text("Outside.\n")
            (self.root / "link.md").symlink_to(target)
            recipe = self.write("root.md", "@link.md\n")
            with self.assertRaisesRegex(MODULE.CompositionError, "escapes kit root"):
                self.composer().resolve(recipe)

    def test_non_directive_text_is_unchanged(self):
        content = "  @missing.md\ntext @missing.md\n@@missing.md\n@\n@missing\n"
        recipe = self.write("root.md", content)
        self.assertEqual(self.composer().resolve(recipe), content)

    def test_nested_relative_paths_and_crlf(self):
        recipe = self.write("root.md", "Title\r\n@parts/child.md\r\n")
        self.write("parts/child.md", "@../shared.md\r\n")
        self.write("shared.md", "Shared.\r\n")
        self.assertEqual(self.composer().resolve(recipe), "Title\r\nShared.\r\n")

    def test_dependency_graph_includes_nested_fragments(self):
        self.write("review.template.md", "@rules.review\n")
        self.write("fragments/rules/review.md", "@rules.writing\n@trust.evidence\n")
        self.write("fragments/rules/writing.md", "Plain language.\n")
        self.write("fragments/trust/evidence.md", "Raw evidence.\n")
        self.config["documents"] = {
            "review.md": {"source": "review.template.md", "depends_on": ["@rules.review"]}
        }
        graph = self.composer().dependency_graph()["review.md"]
        self.assertEqual(graph["direct"], ["@rules.review"])
        self.assertEqual(graph["fragments"], [
            "fragments/rules/review.md", "fragments/rules/writing.md", "fragments/trust/evidence.md"
        ])

    def test_undeclared_and_unused_dependencies_fail(self):
        self.write("review.md", "@rules.review\n")
        self.write("fragments/rules/review.md", "Review.\n")
        for expected in ([], ["@rules.review", "@rules.unused"]):
            with self.subTest(expected=expected):
                self.config["documents"] = {"out.md": {"source": "review.md", "depends_on": expected}}
                with self.assertRaisesRegex(MODULE.CompositionError, "dependency declaration differs"):
                    self.composer().validate()

    def test_failed_scaffold_creates_no_output(self):
        self.write("GOOD.template.md", "Good.\n")
        self.write("BAD.template.md", "@rules.missing\n")
        self.config["documents"] = {
            "GOOD.md": {"source": "GOOD.template.md", "depends_on": []},
            "BAD.md": {"source": "BAD.template.md", "depends_on": ["@rules.missing"]}
        }
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "output"
            with self.assertRaisesRegex(MODULE.CompositionError, "Missing fragment"):
                self.composer().scaffold(output)
            self.assertFalse(output.exists())


class CurrentKitTests(unittest.TestCase):
    def test_current_documents_and_fragments_resolve(self):
        composer = MODULE.Composer(ROOT / "kit/kit.json")
        composer.validate()
        forbidden = ("parameters_and_output_templates", "static_context")
        for name in forbidden:
            self.assertNotIn(name, json.dumps(composer.config))
        with tempfile.TemporaryDirectory() as directory:
            composer.scaffold(directory)
            output = Path(directory)
            self.assertIn("26. Pin every model", (output / "RAILS.md").read_text())
            self.assertIn("## The pointer-dispatch protocol", (output / "dispatches/D-###.md").read_text())
            self.assertIn("## The invariant spine", (output / "dispatches/D-###.result.md").read_text())
            for path in output.rglob("*.md"):
                if path.relative_to(output).parts[0] not in ("fragments", "recipes"):
                    self.assertNotRegex(path.read_text(), r"(?m)^@(charter|workflow|delivery|trust|rules)\.")

    @unittest.skipUnless(shutil.which("git") and shutil.which("jq"), "git and jq required")
    def test_create_kit_records_dependencies_and_composition_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            target = base / "target"
            runs = base / "runs"
            for repo in (target, runs):
                subprocess.run(["git", "init", "-q", str(repo)], check=True)
                subprocess.run(["git", "-C", str(repo), "config", "user.name", "Kit test"], check=True)
                subprocess.run(["git", "-C", str(repo), "config", "user.email", "kit@example.invalid"], check=True)
                subprocess.run(["git", "-C", str(repo), "config", "commit.gpgsign", "false"], check=True)
                subprocess.run(["git", "-C", str(repo), "config", "core.hooksPath", str(base / "no-hooks")], check=True)
            subprocess.run(["git", "-C", str(target), "commit", "-qm", "Initial", "--allow-empty"], check=True)
            result = subprocess.run([
                "sh", str(ROOT / "create/kit"), "--repo", target.as_uri(),
                "--slug", "composition-test", "--orckits", str(runs), "--yes",
            ], text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            manifests = list(runs.rglob("kit.json"))
            self.assertEqual(len(manifests), 1)
            manifest = json.loads(manifests[0].read_text())
            sources = {item["source"] for item in manifest["inputs"]}
            self.assertTrue({"create/kit", "create/compose.py", "kit/kit.json"} <= sources)
            self.assertIn("kit/fragments/trust/supervisor_ledger.md", sources)
            self.assertNotIn("root", manifest)
            self.assertEqual(manifest["documents"]["dispatches/D-###.md"], {
                "source": "recipes/dispatches/D-###.md", "depends_on": ["@trust.supervisor_ledger"]
            })
            self.assertEqual(sum(item["source"] == "kit/kit.json" for item in manifest["inputs"]), 1)
            MODULE.Composer(manifests[0]).validate()
            source = ROOT / "kit/RAILS.template.md"
            expected = MODULE.Composer(ROOT / "kit/kit.json").resolve(source)
            self.assertEqual((manifests[0].parent / "RAILS.md").read_text(), expected)


if __name__ == "__main__":
    unittest.main()
