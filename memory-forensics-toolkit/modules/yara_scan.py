import yara

def scan_dump(dump_path, rules_path):
    print("🧪 Running YARA scan...")
    rules = yara.compile(filepath=rules_path)

    with open(dump_path, "rb") as f:
        data = f.read()
        matches = rules.match(data=data)

    return [str(m) for m in matches]
