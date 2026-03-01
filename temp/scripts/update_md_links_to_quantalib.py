from pathlib import Path

ROOT = Path(r"c:/github/pinescript")
OLD = "https://github.com/mihakralj/pinescript/blob/main/"
NEW = "https://github.com/mihakralj/QuanTAlib/blob/main/"

def main() -> None:
    md_files = sorted(ROOT.rglob("*.md"))
    changed = 0
    replacements = 0

    for p in md_files:
        text = p.read_text(encoding="utf-8")
        count = text.count(OLD)
        if count == 0:
            continue

        updated = text.replace(OLD, NEW)
        p.write_text(updated, encoding="utf-8")
        changed += 1
        replacements += count

    print(f"TOTAL_MD {len(md_files)}")
    print(f"FILES_CHANGED {changed}")
    print(f"LINKS_REWRITTEN {replacements}")

if __name__ == "__main__":
    main()