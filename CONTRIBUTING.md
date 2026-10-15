# Contributing

1. Add one object to `plugins` in `catalog/plugins.json` with: `name` (kebab-case, unique), `description` (10-200 chars, written in your own words), `category` (see the enum in `schema/plugins.schema.json`), `homepage` (https), `source` (`https://github.com/owner/repo`), `keywords` (lowercase, unique).
2. Use only facts from the project's own public pages. Do not copy README text, logos or skill files from other repositories.
3. Run `python3 scripts/validate.py` and `python3 scripts/generate_index.py`, then commit `catalog/index.json` too.
4. Open a PR; the `validate-catalog` workflow must pass.

การเพิ่มรายการ: เขียนคำอธิบายเอง ห้ามคัดลอกข้อความหรือโลโก้จาก repo อื่น และรันสคริปต์ตรวจก่อนเปิด PR
