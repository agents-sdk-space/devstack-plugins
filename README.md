# devstack-plugins

Plugin and MCP server catalog for [devstack.bid](https://devstack.bid) (NVX Stack Builder).

**EN:** `catalog/plugins.json` lists third-party plugins/MCP servers by name, short description, category, homepage, source repo and keywords. It is metadata only: nothing here is installed or executed by devstack.bid. Each listed project has its own license and terms.

**TH:** `catalog/plugins.json` คือรายการปลั๊กอิน/MCP server ภายนอก มีชื่อ คำอธิบายสั้น หมวด หน้าเว็บ repo ต้นทาง และคีย์เวิร์ด เป็นข้อมูลอ้างอิงเท่านั้น devstack.bid ไม่ได้ติดตั้งหรือรันโค้ดใดๆ แต่ละโปรเจกต์มีสัญญาอนุญาตของตัวเอง

```bash
python3 scripts/validate.py          # validate the catalog / ตรวจรายการ
python3 scripts/generate_index.py    # regenerate catalog/index.json
```

Schema: `schema/plugins.schema.json` · Contributing: [CONTRIBUTING.md](CONTRIBUTING.md) · License: MIT (covers this repo's own files only).
