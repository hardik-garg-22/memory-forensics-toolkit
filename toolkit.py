import argparse
from modules import acquisition, analysis, yara_scan, report

def main():
    parser = argparse.ArgumentParser(description="Memory Forensics Toolkit")
    parser.add_argument("--dump", help="Path to memory dump file")
    parser.add_argument("--yara", help="Path to YARA rules file")
    parser.add_argument("--report", help="Path to save report", default="reports/report.json")
    args = parser.parse_args()

    if not args.dump:
        print("❌ Please provide a memory dump file (--dump).")
        return

    print("🔹 Starting Memory Forensics Toolkit...")

    findings = analysis.run_volatility(args.dump)

    if args.yara:
        yara_hits = yara_scan.scan_dump(args.dump, args.yara)
        findings["yara_matches"] = yara_hits

    report.generate_report(findings, args.report)
    print(f"✅ Analysis complete. Report saved at {args.report}")

if __name__ == "__main__":
    main()
