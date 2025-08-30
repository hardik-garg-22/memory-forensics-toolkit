# 🛡️ Memory Forensics Toolkit

## Overview
A Python-based toolkit for analyzing memory dumps to detect malware, hidden processes, and forensic artifacts.

## Features
- Acquire memory dumps (DumpIt, LiME, AVML)
- Analyze using Volatility3 plugins
- YARA scanning for malware patterns
- JSON and PDF report generation

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python toolkit.py --dump dumps/sample.vmem --yara rules/malware_rules.yar --report reports/report.json
```

## Output
- JSON: `reports/report.json`
- PDF: `reports/report.pdf`
