#!/usr/bin/env python3
"""Generate catalog/index.json (plugins grouped by category, sorted). Use --check in CI."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "catalog/index.json"

def build() -> str:
    data = json.loads((ROOT / "catalog/plugins.json").read_text(encoding="utf-8"))
    cats: dict[str, list[str]] = {}
    for p in data["plugins"]:
        cats.setdefault(p["category"], []).append(p["name"])
    index = {"count": len(data["plugins"]), "categories": {c: sorted(v) for c, v in sorted(cats.items())}}
    return json.dumps(index, indent=2, ensure_ascii=False) + "\n"

def main() -> int:
    text = build()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("catalog/index.json is stale; run: python3 scripts/generate_index.py"); return 1
        print("OK: index up to date"); return 0
    OUT.write_text(text, encoding="utf-8"); print(f"wrote {OUT.relative_to(ROOT)}"); return 0

if __name__ == "__main__":
    sys.exit(main())
