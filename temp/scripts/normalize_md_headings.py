from pathlib import Path
import re

ROOT = Path(r"c:/github/pinescript")

IND_RE = re.compile(r'^\s*indicator\(\s*"([^"]+)"\s*,\s*"([^"]+)"')
LIB_RE = re.compile(r'^\s*library\(\s*"([^"]+)"')

def title_from_stem(stem: str) -> str:
    return stem.replace("_", " ").replace("-", " ").title()

def clean_full_name(full: str, short: str) -> str:
    token = f"({short})"
    if token in full:
        full = full.replace(token, "")
    return full.strip(" -")

def infer_from_pine(md_path: Path) -> tuple[str, str] | None:
    pine = md_path.with_suffix(".pine")
    if not pine.exists():
        return None

    text = pine.read_text(encoding="utf-8")
    m = IND_RE.search(text)
    if m:
        full = m.group(1).strip()
        short = m.group(2).strip().upper()
        full = clean_full_name(full, short) or title_from_stem(md_path.stem)
        return short, full

    m = LIB_RE.search(text)
    if m:
        full = m.group(1).strip() or title_from_stem(md_path.stem)
        short = md_path.stem.upper()
        return short, full

    return None

def fallback(md_path: Path) -> tuple[str, str]:
    short = md_path.stem.upper()
    full = title_from_stem(md_path.stem)
    return short, full

def normalize(md_path: Path) -> bool:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    inferred = infer_from_pine(md_path)
    short, full = inferred if inferred is not None else fallback(md_path)
    heading = f"# {short} - {full}"

    idx = None
    for i, line in enumerate(lines):
        if line.strip():
            idx = i
            break

    if idx is None:
        new_text = heading + "\n"
    else:
        first = lines[idx].strip()
        if first.startswith("# "):
            lines[idx] = heading
            new_text = "\n".join(lines).rstrip() + "\n"
        else:
            prefix = lines[:idx]
            suffix = lines[idx:]
            new_lines = prefix + [heading, ""] + suffix
            new_text = "\n".join(new_lines).rstrip() + "\n"

    if new_text != text:
        md_path.write_text(new_text, encoding="utf-8")
        return True
    return False

def main() -> None:
    md_files = sorted(ROOT.rglob("*.md"))
    changed = 0
    for md in md_files:
        if normalize(md):
            changed += 1

    print(f"TOTAL_MD {len(md_files)}")
    print(f"FILES_CHANGED {changed}")

if __name__ == "__main__":
    main()