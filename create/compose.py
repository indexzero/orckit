#!/usr/bin/env python3
"""Compose Markdown using fragment conventions and declared document roots."""

import argparse
import json
from pathlib import Path
import re
import sys


REFERENCE = re.compile(r"@(?P<area>[a-z][a-z0-9_]*)\.(?P<fragment_name>[a-z][a-z0-9_]*)")
CONVENTION = "@{{area}}.{{fragment_name}}"
FRAGMENT_PATH = "./fragments/{{area}}/{{fragment_name}}.md"


class CompositionError(ValueError):
    pass


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise CompositionError(f"Duplicate manifest key: {key}")
        result[key] = value
    return result


class Composer:
    def __init__(self, manifest):
        self.manifest_path = Path(manifest).resolve()
        self.config = json.loads(
            self.manifest_path.read_text(encoding="utf-8"),
            object_pairs_hook=unique_keys,
        )
        if not isinstance(self.config, dict):
            raise CompositionError("Manifest must be an object")
        self.root = self.manifest_path.parent
        conventions = self.config.get("conventions", {})
        if not isinstance(conventions, dict) or set(conventions) - {CONVENTION}:
            raise CompositionError(f"Only the {CONVENTION} convention is supported")
        self.fragment_pattern = conventions.get(CONVENTION, FRAGMENT_PATH)
        if not isinstance(self.fragment_pattern, str) or any(
            self.fragment_pattern.count("{{" + field + "}}") != 1
            for field in ("area", "fragment_name")
        ):
            raise CompositionError("Fragment convention must contain area and fragment_name once")
        self.documents = self.config.get("documents", {})
        if not isinstance(self.documents, dict):
            raise CompositionError("documents must map rendered filenames to source recipes")

    def source_path(self, value, base):
        path = Path(value)
        if path.is_absolute() or path.suffix != ".md":
            raise CompositionError(f"Expected a relative Markdown path: {value}")
        path = (base / path).resolve()
        if not path.is_relative_to(self.root):
            raise CompositionError(f"Reference escapes kit root: {value}")
        if not path.is_file():
            raise CompositionError(f"Missing fragment or recipe: {path}")
        return path

    def reference_path(self, reference, source):
        token = reference[1:] if reference.startswith("@") else ""
        if token.endswith(".md") and not token.startswith(("@", " ", "\t")):
            return self.source_path(token, source.parent)
        match = REFERENCE.fullmatch(reference)
        if match:
            path = self.fragment_pattern
            for key, value in match.groupdict().items():
                path = path.replace("{{" + key + "}}", value)
            return self.source_path(path, self.root)
        return None

    def source_lines(self, source):
        source = Path(source).resolve()
        if not source.is_relative_to(self.root):
            raise CompositionError(f"Source escapes kit root: {source}")
        return source.read_bytes().decode("utf-8").splitlines(keepends=True)

    def references(self, source):
        references = []
        for number, line in enumerate(self.source_lines(source), 1):
            reference = line.rstrip("\r\n")
            try:
                path = self.reference_path(reference, source)
            except CompositionError as error:
                raise CompositionError(f"{source}:{number}: {error}") from error
            if path is not None:
                references.append((number, reference, path))
        return references

    def resolve(self, source, ancestors=(), dependencies=None):
        source = Path(source).resolve()
        if source in ancestors:
            cycle = " -> ".join(str(p.relative_to(self.root)) for p in (*ancestors, source))
            raise CompositionError(f"Circular reference: {cycle}")
        ancestors = (*ancestors, source)
        output = []
        for number, line in enumerate(self.source_lines(source), 1):
            try:
                path = self.reference_path(line.rstrip("\r\n"), source)
                if path is None:
                    output.append(line)
                    continue
                if dependencies is not None:
                    dependencies.add(str(path.relative_to(self.root)))
                expanded = self.resolve(path, ancestors, dependencies)
                if line.endswith("\n") and expanded and not expanded.endswith("\n"):
                    expanded += "\r\n" if line.endswith("\r\n") else "\n"
                output.append(expanded)
            except (CompositionError, OSError, UnicodeError) as error:
                raise CompositionError(f"{source}:{number}: {error}") from error
        return "".join(output)

    def document_sources(self):
        outputs = set()
        for name, document in self.documents.items():
            output = Path(name)
            if (output.is_absolute() or ".." in output.parts or output.suffix != ".md"
                    or output.parts[0] in ("fragments", "recipes")):
                raise CompositionError(f"Invalid rendered document path: {name}")
            if output in outputs:
                raise CompositionError(f"Duplicate output path: {name}")
            outputs.add(output)
            if not isinstance(document, dict) or not isinstance(document.get("source"), str):
                raise CompositionError(f"Missing source recipe: {name}")
            expected = document.get("depends_on")
            if (not isinstance(expected, list) or any(not isinstance(ref, str) for ref in expected)
                    or len(expected) != len(set(expected))):
                raise CompositionError(f"Expected unique depends_on references: {name}")
            source = self.source_path(document["source"], self.root)
            actual = list(dict.fromkeys(ref for _, ref, _ in self.references(source)))
            missing = sorted(set(actual) - set(expected))
            extra = sorted(set(expected) - set(actual))
            if missing or extra:
                raise CompositionError(
                    f"{name}: dependency declaration differs from recipe; "
                    f"undeclared={missing}, unused={extra}"
                )
            yield name, source, actual

    def dependency_graph(self):
        graph = {}
        for name, source, direct in self.document_sources():
            dependencies = set()
            self.resolve(source, dependencies=dependencies)
            graph[name] = {
                "source": str(source.relative_to(self.root)),
                "direct": direct,
                "fragments": sorted(dependencies),
            }
        return graph

    def validate(self):
        self.dependency_graph()
        # Check unused fragments too, so a broken library member stays visible.
        for path in sorted((self.root / "fragments").rglob("*.md")):
            self.resolve(path)

    def scaffold(self, output_dir):
        output_dir = Path(output_dir).resolve()
        if output_dir == self.root or output_dir.is_relative_to(self.root):
            raise CompositionError("Output directory must be outside the source kit")
        if not self.documents:
            raise CompositionError("No rendered documents declared")
        self.validate()
        outputs = {}
        for source in sorted((self.root / "fragments").rglob("*.md")):
            self.source_lines(source)
            outputs[source.relative_to(self.root)] = source.read_bytes()
        for name, source, _ in self.document_sources():
            outputs[Path(name)] = self.resolve(source).encode("utf-8")
            # Keep the recipes so the run's dependency declarations remain checkable.
            outputs[Path("recipes") / source.relative_to(self.root)] = source.read_bytes()
        for relative, payload in outputs.items():
            destination = output_dir / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", help="Markdown recipe to print")
    parser.add_argument("--manifest", default=str(Path(__file__).resolve().parent.parent / "kit/kit.json"))
    parser.add_argument("--output-dir", help="Scaffold declared documents into this directory")
    parser.add_argument("--check", action="store_true", help="Check declared dependencies and all fragments")
    parser.add_argument("--dependencies", action="store_true", help="Print each document's direct and transitive dependencies")
    args = parser.parse_args()
    if sum((bool(args.source), bool(args.output_dir), args.check, args.dependencies)) != 1:
        parser.error("Choose a source, --output-dir, --check, or --dependencies")
    try:
        composer = Composer(args.manifest)
        if args.check:
            composer.validate()
        elif args.dependencies:
            print(json.dumps(composer.dependency_graph(), indent=2))
        elif args.output_dir:
            composer.scaffold(args.output_dir)
        else:
            sys.stdout.buffer.write(composer.resolve(args.source).encode("utf-8"))
    except (CompositionError, OSError, UnicodeError) as error:
        print(f"compose: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
