from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_report(output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    c.drawString(100, 800, 'Raport analizy gleby')
    c.showPage()
    c.save()

if __name__ == '__main__':
    generate_report('../SmartAgro_report.pdf')
