#!/usr/bin/env python3
"""Validate catalog/plugins.json against the rules in schema/plugins.schema.json (stdlib only)."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def main() -> int:
    schema = json.loads((ROOT / "schema/plugins.schema.json").read_text(encoding="utf-8"))
    item = schema["properties"]["plugins"]["items"]
    props, required = item["properties"], item["required"]
    try:
        data = json.loads((ROOT / "catalog/plugins.json").read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"catalog/plugins.json: invalid JSON: {e}"); return 1
    errs = []
    for k in schema["required"]:
        if k not in data: errs.append(f"top-level: missing '{k}'")
    for k in data:
        if k not in schema["properties"]: errs.append(f"top-level: unknown key '{k}'")
    plugins = data.get("plugins")
    if not isinstance(plugins, list): errs.append("'plugins' must be an array"); plugins = []
    seen = set()
    for i, p in enumerate(plugins):
        where = f"plugins[{i}] ({p.get('name', '?') if isinstance(p, dict) else '?'})"
        if not isinstance(p, dict): errs.append(f"{where}: must be an object"); continue
        for k in required:
            if k not in p: errs.append(f"{where}: missing '{k}'")
        for k, v in p.items():
            rule = props.get(k)
            if rule is None: errs.append(f"{where}: unknown key '{k}'"); continue
            if rule.get("type") == "array":
                if not isinstance(v, list) or len(v) < rule.get("minItems", 0):
                    errs.append(f"{where}: '{k}' must be a non-empty array"); continue
                if rule.get("uniqueItems") and len(set(map(str, v))) != len(v):
                    errs.append(f"{where}: '{k}' has duplicates")
                pat = rule["items"].get("pattern")
                for x in v:
                    if not isinstance(x, str) or (pat and not re.search(pat, x)):
                        errs.append(f"{where}: bad {k} item {x!r}")
                continue
            if not isinstance(v, str): errs.append(f"{where}: '{k}' must be a string"); continue
            if "enum" in rule and v not in rule["enum"]: errs.append(f"{where}: '{k}' not in {rule['enum']}")
            if "pattern" in rule and not re.search(rule["pattern"], v): errs.append(f"{where}: '{k}' does not match {rule['pattern']}")
            if len(v) < rule.get("minLength", 0) or len(v) > rule.get("maxLength", 10**9):
                errs.append(f"{where}: '{k}' length out of range")
        n = p.get("name")
        if n in seen: errs.append(f"{where}: duplicate name")
        seen.add(n)
    if errs:
        print("Catalog validation failed:"); [print("  -", e) for e in errs]; return 1
    print(f"OK: {len(plugins)} plugins valid"); return 0

if __name__ == "__main__":
    sys.exit(main())
