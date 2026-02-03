from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io


def generate_summary_pdf(summary):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Chemical Equipment Analysis Report")

    pdf.setFont("Helvetica", 12)
    y -= 40

    lines = [
        f"Total Equipment: {summary['total_equipment']}",
        f"Average Flowrate: {summary['average_flowrate']:.2f}",
        f"Average Pressure: {summary['average_pressure']:.2f}",
        f"Max Temperature: {summary['max_temperature']}",
        "",
        "Equipment Type Distribution:"
    ]

    for line in lines:
        pdf.drawString(50, y, line)
        y -= 20

    for k, v in summary["equipment_type_distribution"].items():
        pdf.drawString(70, y, f"{k}: {v}")
        y -= 18

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer
