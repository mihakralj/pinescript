from pathlib import Path
import re

ROOT = Path(r"c:/github/pinescript")

CATEGORY_TITLES = {
    "channels": "Channels and Bands",
    "core": "Core Price Transforms",
    "cycles": "Cycles",
    "dynamics": "Dynamics",
    "errors": "Error Metrics",
    "filters": "Filters",
    "forecasts": "Forecasts",
    "momentum": "Momentum",
    "numerics": "Numerics",
    "oscillators": "Oscillators",
    "reversals": "Reversals",
    "statistics": "Statistics",
    "trends_FIR": "Trends - FIR",
    "trends_IIR": "Trends - IIR",
    "volatility": "Volatility",
    "volume": "Volume",
}

ROW_RE = re.compile(r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+?)\s*\|")

def main() -> None:
    lines: list[str] = []
    for cat in sorted(CATEGORY_TITLES.keys(), key=lambda k: CATEGORY_TITLES[k].lower()):
        idx = ROOT / "indicators" / cat / "_index.md"
        if not idx.exists():
            continue

        lines.append(f"* [{CATEGORY_TITLES[cat]}](/indicators/{cat}/_index.md)")

        for raw in idx.read_text(encoding="utf-8").splitlines():
            m = ROW_RE.match(raw.strip())
            if not m:
                continue

            code = m.group(1).strip()
            link = m.group(2).strip()
            name = m.group(3).strip()

            if not link.startswith("/"):
                link = "/" + link.lstrip("./")

            lines.append(f"  * [{code}: {name}]({link})")

        lines.append("")

    target = ROOT / "_sidebar.md"
    target.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Updated {target.as_posix()}")

if __name__ == "__main__":
    main()