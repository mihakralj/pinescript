from pathlib import Path

ROOT = Path(r"c:/github/pinescript")

def main() -> None:
    md_files = sorted(ROOT.rglob("*.md"))
    changed = 0
    removed = 0

    for p in md_files:
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines()

        out = []
        local_removed = 0

        for line in lines:
            if line.strip().startswith("[Pine Script implementation]("):
                local_removed += 1
                continue
            out.append(line)

        if local_removed > 0:
            changed += 1
            removed += local_removed
            p.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")

    print(f"TOTAL_MD {len(md_files)}")
    print(f"FILES_CHANGED {changed}")
    print(f"LINES_REMOVED {removed}")

if __name__ == "__main__":
    main()