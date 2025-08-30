import json
from fpdf import FPDF

def generate_report(findings, report_path):
    with open(report_path, "w") as f:
        json.dump(findings, f, indent=4)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Memory Forensics Report", ln=True, align="C")
    pdf.ln(10)

    for section, data in findings.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt=section.upper(), ln=True)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, txt=json.dumps(data, indent=2)[:1000])
        pdf.ln(5)

    pdf.output(report_path.replace(".json", ".pdf"))
