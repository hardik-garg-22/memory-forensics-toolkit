import subprocess, json

def run_volatility(dump_path):
    print("🔎 Running Volatility3 analysis...")

    plugins = ["windows.pslist", "windows.netscan", "windows.dlllist", "windows.malfind"]
    results = {}

    for plugin in plugins:
        try:
            cmd = ["volatility3", "-f", dump_path, plugin, "--output", "json"]
            output = subprocess.check_output(cmd, text=True)
            results[plugin] = json.loads(output) if output else {}
        except Exception as e:
            results[plugin] = {"error": str(e)}

    return results
