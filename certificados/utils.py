import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from django.conf import settings
from reportlab.lib import colors
from reportlab.lib.units import cm

def gerar_pdf_certificado(nome, curso, data_emissao, arquivo_nome):
    caminho_pasta = os.path.join(settings.MEDIA_ROOT, 'certificados')
    os.makedirs(caminho_pasta, exist_ok=True)
    
    caminho_arquivo = os.path.join(caminho_pasta, arquivo_nome)
    
    c = canvas.Canvas(caminho_arquivo, pagesize=landscape(A4))
    largura, altura = landscape(A4)

    # Fundo colorido
    c.setFillColorRGB(0.95, 0.95, 1)  # azul claro
    c.rect(0, 0, largura, altura, fill=1)

    # Borda decorativa
    c.setStrokeColor(colors.darkblue)
    c.setLineWidth(4)
    c.rect(1*cm, 1*cm, largura - 2*cm, altura - 2*cm)

    # Título
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(colors.darkblue)
    c.drawCentredString(largura / 2, altura - 80, "Certificado de Conclusão")

    # Texto principal
    c.setFont("Helvetica", 16)
    c.setFillColor(colors.black)
    c.drawCentredString(largura / 2, altura - 150, f"Certificamos que")
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(largura / 2, altura - 185, nome)
    c.setFont("Helvetica", 16)
    c.drawCentredString(largura / 2, altura - 220, f"concluiu com êxito o curso:")
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(largura / 2, altura - 255, curso)
    c.setFont("Helvetica", 16)
    c.drawCentredString(largura / 2, altura - 290, f"em {data_emissao}")

    # Rodapé
    c.setFont("Helvetica-Oblique", 12)
    c.setFillColor(colors.grey)
    c.drawCentredString(largura / 2, 40, "Este certificado foi gerado automaticamente.")

    c.save()
    return f'certificados/{arquivo_nome}'