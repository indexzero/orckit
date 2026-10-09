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
        self.bindings = {group: {} for group in MODULE.GROUPS}

    def write(self, path, text):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(text.encode("utf-8"))
        return file

    def composer(self):
        self.manifest.write_text(json.dumps(self.bindings))
        return MODULE.Composer(self.manifest)

    def test_binding_can_change_without_editing_recipe(self):
        recipe = self.write("review.md", "# Review\n@rules.writing\n")
        self.write("plain.md", "Plain language.\n")
        self.write("technical.md", "Technical English.\n")
        self.bindings["rules"]["writing"] = "plain.md"
        self.assertEqual(self.composer().resolve(recipe), "# Review\nPlain language.\n")
        self.bindings["rules"]["writing"] = "technical.md"
        self.assertEqual(self.composer().resolve(recipe), "# Review\nTechnical English.\n")

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

    def test_ordered_binding_and_fragment_whitespace(self):
        recipe = self.write("root.md", "Before\n@charter.context\nAfter\n")
        self.write("first.md", "\nFirst.\n\n")
        self.write("second.md", "Second.")
        self.bindings["charter"]["context"] = ["first.md", "second.md"]
        self.assertEqual(self.composer().resolve(recipe), "Before\n\nFirst.\n\nSecond.\nAfter\n")

    def test_unknown_binding_fails_with_source_location(self):
        recipe = self.write("root.md", "Title\n@rules.missing\n")
        with self.assertRaisesRegex(MODULE.CompositionError, r"root.md:2: Unknown responsibility"):
            self.composer().resolve(recipe)

    def test_missing_fragment_fails(self):
        recipe = self.write("root.md", "@missing.md\n")
        with self.assertRaisesRegex(MODULE.CompositionError, "Missing fragment"):
            self.composer().resolve(recipe)

    def test_duplicate_manifest_key_fails(self):
        self.manifest.write_text('{"rules": {}, "rules": {}}')
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
            with self.assertRaisesRegex(MODULE.CompositionError, "escapes manifest directory"):
                self.composer().resolve(recipe)

    def test_non_directive_text_is_unchanged(self):
        content = "  @missing.md\ntext @missing.md\n@@missing.md\n@\n@missing.txt\n"
        recipe = self.write("root.md", content)
        self.assertEqual(self.composer().resolve(recipe), content)

    def test_nested_relative_paths_and_crlf(self):
        recipe = self.write("root.md", "Title\r\n@parts/child.md\r\n")
        self.write("parts/child.md", "@../shared.md\r\n")
        self.write("shared.md", "Shared.\r\n")
        self.assertEqual(self.composer().resolve(recipe), "Title\r\nShared.\r\n")

    def test_failed_scaffold_creates_no_output(self):
        self.write("kit/GOOD.template.md", "Good.\n")
        self.write("kit/BAD.template.md", "@missing.md\n")
        output = self.root / "output"
        with self.assertRaises(MODULE.CompositionError):
            self.composer().scaffold(self.root / "kit", output)
        self.assertFalse(output.exists())


class CurrentKitTests(unittest.TestCase):
    def test_current_bindings_and_templates_resolve(self):
        composer = MODULE.Composer(ROOT / "kit.example.json")
        composer.validate()
        forbidden = ("parameters_and_output_templates", "static_context")
        for name in forbidden:
            self.assertNotIn(name, json.dumps(composer.bindings))
        with tempfile.TemporaryDirectory() as directory:
            composer.scaffold(ROOT / "kit", directory)
            output = Path(directory)
            self.assertIn("26. Pin every model", (output / "RAILS.md").read_text())
            self.assertIn("## The pointer-dispatch protocol", (output / "dispatches/D-###.md").read_text())
            self.assertIn("## The invariant spine", (output / "dispatches/D-###.result.md").read_text())
            for path in output.rglob("*.md"):
                if "fragments" not in path.relative_to(output).parts:
                    self.assertNotRegex(path.read_text(), r"(?m)^@(charter|workflow|delivery|trust|rules)\.")

    @unittest.skipUnless(shutil.which("git") and shutil.which("jq"), "git and jq required")
    def test_create_kit_records_bindings_and_composition_inputs(self):
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
            self.assertTrue({"create/kit", "create/compose.py", "kit.example.json"} <= sources)
            self.assertIn("kit/fragments/trust/supervisor-ledger.md", sources)
            self.assertEqual(manifest["trust"]["supervisor_ledger"], "fragments/trust/supervisor-ledger.md")
            MODULE.Composer(manifests[0]).validate()
            source = ROOT / "kit/RAILS.template.md"
            expected = MODULE.Composer(ROOT / "kit.example.json").resolve(source)
            self.assertEqual((manifests[0].parent / "RAILS.md").read_text(), expected)


if __name__ == "__main__":
    unittest.main()
