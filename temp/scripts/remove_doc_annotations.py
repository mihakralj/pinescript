from pathlib import Path

ROOT = Path(r"c:/github/pinescript")

def main() -> None:
    files = sorted(ROOT.rglob("*.pine"))
    changed = 0
    removed = 0

    for p in files:
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines()
        kept = []
        local_removed = 0

        for line in lines:
            if line.strip().startswith("//@doc "):
                local_removed += 1
                continue
            kept.append(line)

        if local_removed > 0:
            changed += 1
            removed += local_removed
            p.write_text("\n".join(kept).rstrip() + "\n", encoding="utf-8")

    print(f"TOTAL_FILES {len(files)}")
    print(f"FILES_CHANGED {changed}")
    print(f"DOC_LINES_REMOVED {removed}")

if __name__ == "__main__":
    main()