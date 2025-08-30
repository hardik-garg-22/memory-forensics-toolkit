import subprocess
import os

def acquire_memory(output_file="dumps/memdump.raw", tool="dumpit"):
    print("📝 Starting memory acquisition...")

    if tool.lower() == "dumpit":
        if os.name != "nt":
            return "❌ DumpIt is Windows-only."
        cmd = ["DumpIt.exe", output_file]
        subprocess.run(cmd)

    elif tool.lower() == "lime":
        print("⚡ Use: insmod lime.ko path=/tmp/memdump.lime format=lime")

    elif tool.lower() == "avml":
        cmd = ["avml", output_file]
        subprocess.run(cmd)

    else:
        return "❌ Unknown tool selected."

    return f"✅ Memory dump saved at {output_file}"
