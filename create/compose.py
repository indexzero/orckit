#!/usr/bin/env python3
"""Compose Markdown from responsibility bindings and relative file references."""

import argparse
import json
from pathlib import Path
import re
import sys


GROUPS = ("charter", "workflow", "delivery", "trust", "rules")
ADDRESS = re.compile(r"[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+")


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
        self.root = self.manifest_path.parent
        self.bindings = json.loads(
            self.manifest_path.read_text(encoding="utf-8"),
            object_pairs_hook=unique_keys,
        )

    def source_path(self, value, base):
        path = Path(value)
        if path.is_absolute() or path.suffix != ".md":
            raise CompositionError(f"Expected a relative Markdown path: {value}")
        path = (base / path).resolve()
        if not path.is_relative_to(self.root):
            raise CompositionError(f"Reference escapes manifest directory: {value}")
        if not path.is_file():
            raise CompositionError(f"Missing fragment: {path}")
        return path

    def bound_paths(self, address):
        parts = address.split(".")
        value = self.bindings
        if parts[0] not in GROUPS:
            raise CompositionError(f"Unknown responsibility: {address}")
        for part in parts:
            if not isinstance(value, dict) or part not in value:
                raise CompositionError(f"Unknown responsibility: {address}")
            value = value[part]
        values = [value] if isinstance(value, str) else value
        if not isinstance(values, list) or not values:
            raise CompositionError(f"Expected fragment binding: {address}")
        if any(not isinstance(item, str) for item in values):
            raise CompositionError(f"Expected fragment paths: {address}")
        return [self.source_path(item, self.root) for item in values]

    def resolve(self, source, ancestors=()):
        source = Path(source).resolve()
        if not source.is_relative_to(self.root):
            raise CompositionError(f"Source escapes manifest directory: {source}")
        if source in ancestors:
            cycle = " -> ".join(str(p.relative_to(self.root)) for p in (*ancestors, source))
            raise CompositionError(f"Circular reference: {cycle}")
        # Each inclusion has its own ancestry. Siblings may reuse a fragment.
        ancestors = (*ancestors, source)
        content = source.read_bytes().decode("utf-8")
        output = []
        for number, line in enumerate(content.splitlines(keepends=True), 1):
            text = line.rstrip("\r\n")
            token = text[1:] if text.startswith("@") else ""
            try:
                if token.endswith(".md") and not token.startswith(("@", " ", "\t")):
                    paths = [self.source_path(token, source.parent)]
                elif ADDRESS.fullmatch(token) and token.split(".")[0] in GROUPS:
                    paths = self.bound_paths(token)
                else:
                    output.append(line)
                    continue
                fragments = [self.resolve(path, ancestors) for path in paths]
                # Preserve fragment whitespace, adding only missing boundaries.
                expanded = ""
                for fragment in fragments:
                    if expanded and not expanded.endswith(("\n", "\r")):
                        expanded += "\n"
                    expanded += fragment
                if line.endswith("\n") and expanded and not expanded.endswith("\n"):
                    expanded += "\r\n" if line.endswith("\r\n") else "\n"
                output.append(expanded)
            except (CompositionError, OSError, UnicodeError) as error:
                raise CompositionError(f"{source}:{number}: {error}") from error
        return "".join(output)

    def validate(self):
        def visit(value, parts):
            if isinstance(value, dict):
                for key, child in value.items():
                    visit(child, (*parts, key))
            else:
                for path in self.bound_paths(".".join(parts)):
                    self.resolve(path)

        for group in GROUPS:
            if not isinstance(self.bindings.get(group), dict):
                raise CompositionError(f"Missing responsibility group: {group}")
            visit(self.bindings[group], (group,))

    def scaffold(self, kit_dir, output_dir):
        kit_dir = Path(kit_dir).resolve()
        output_dir = Path(output_dir).resolve()
        if not kit_dir.is_dir():
            raise CompositionError(f"Missing source kit: {kit_dir}")
        if output_dir == kit_dir or output_dir.is_relative_to(kit_dir):
            raise CompositionError("Output directory must be outside the source kit")
        self.validate()
        outputs = {}
        for source in sorted(kit_dir.rglob("*")):
            if not source.is_file():
                continue
            relative = source.relative_to(kit_dir)
            if relative.parts[0] == "fragments" or source.suffix != ".md":
                payload = source.read_bytes()
            else:
                payload = self.resolve(source).encode("utf-8")
                relative = relative.with_name(relative.name.replace(".template.md", ".md"))
            if relative in outputs:
                raise CompositionError(f"Duplicate output path: {relative}")
            outputs[relative] = payload
        # Resolve everything before creating output files.
        for relative, payload in outputs.items():
            destination = output_dir / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", help="Markdown recipe to print")
    parser.add_argument("--manifest", default=str(Path(__file__).resolve().parent.parent / "kit.example.json"))
    parser.add_argument("--output-dir", help="Scaffold all kit recipes into this directory")
    parser.add_argument("--check", action="store_true", help="Validate every responsibility binding")
    args = parser.parse_args()
    if sum((bool(args.source), bool(args.output_dir), args.check)) != 1:
        parser.error("Choose a source, --output-dir, or --check")
    try:
        composer = Composer(args.manifest)
        if args.check:
            composer.validate()
        elif args.output_dir:
            composer.scaffold(composer.root / "kit", args.output_dir)
        else:
            sys.stdout.buffer.write(composer.resolve(args.source).encode("utf-8"))
    except (CompositionError, OSError, UnicodeError) as error:
        print(f"compose: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
