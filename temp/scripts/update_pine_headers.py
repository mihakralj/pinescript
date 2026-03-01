from pathlib import Path
import re

ROOT = Path(r"c:/github/pinescript")

STANDARD_HEADER = [
    "// The MIT License (MIT)",
    "// © mihakralj",
    "//@version=6",
]

DECL_RE = re.compile(r"^\s*(indicator|library)\s*\(")


def normalize_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    decl_idx = None
    for i, line in enumerate(lines):
        if DECL_RE.match(line):
            decl_idx = i
            break

    if decl_idx is None:
        return False

    declaration = lines[decl_idx].strip()
    tail = lines[decl_idx + 1 :]

    # Trim leading blank lines from tail so there is exactly one blank line after declaration.
    while tail and tail[0].strip() == "":
        tail = tail[1:]

    new_lines = []
    new_lines.extend(STANDARD_HEADER)
    new_lines.append(declaration)
    new_lines.append("")
    new_lines.extend(tail)

    new_text = "\n".join(new_lines).rstrip() + "\n"
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> None:
    pine_files = sorted(ROOT.rglob("*.pine"))
    changed = 0

    for p in pine_files:
        if normalize_file(p):
            changed += 1

    print(f"Processed {len(pine_files)} .pine files")
    print(f"Updated headers in {changed} files")


if __name__ == "__main__":
    main()