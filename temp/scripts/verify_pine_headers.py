from pathlib import Path
import re

ROOT = Path(r"c:/github/pinescript")
DECL_RE = re.compile(r"^(indicator|library)\s*\(")

def main() -> None:
    files = sorted(ROOT.rglob("*.pine"))
    bad: list[str] = []

    for p in files:
        lines = p.read_text(encoding="utf-8").splitlines()
        ok = (
            len(lines) >= 4
            and lines[0] == "// The MIT License (MIT)"
            and lines[1] == "// © mihakralj"
            and lines[2] == "//@version=6"
            and DECL_RE.match(lines[3].strip()) is not None
        )
        if not ok:
            bad.append(p.as_posix().replace("c:/github/pinescript/", ""))

    print(f"TOTAL {len(files)}")
    print(f"COMPLIANT {len(files) - len(bad)}")
    print(f"NON_COMPLIANT {len(bad)}")
    for path in bad[:20]:
        print(path)

if __name__ == "__main__":
    main()