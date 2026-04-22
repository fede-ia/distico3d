from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.units import inch, cm
from PyPDF2 import PdfReader
import re
import os

# Configuración de estilos
def setup_styles():
    styles = getSampleStyleSheet()
    
    # Estilo para títulos principales
    styles.add(ParagraphStyle(
        name='MainTitle',
        fontSize=24,
        leading=28,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#0a0a0a'),
        alignment=1,  # Centrado
        spaceAfter=20
    ))
    
    # Estilo para subtítulos
    styles.add(ParagraphStyle(
        name='Subtitle',
        fontSize=18,
        leading=22,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#7b2cbf'),
        alignment=1,
        spaceAfter=15
    ))
    
    # Estilo para texto normal
    styles.add(ParagraphStyle(
        name='BodyText',
        fontSize=12,
        leading=16,
        fontName='Helvetica',
        textColor=colors.HexColor('#4a4a4a'),
        spaceAfter=12
    ))
    
    # Estilo para listas
    styles.add(ParagraphStyle(
        name='Bullet',
        fontSize=12,
        leading=16,
        fontName='Helvetica',
        textColor=colors.HexColor('#4a4a4a'),
        leftIndent=20,
        spaceAfter=8
    ))
    
    return styles

def process_pdf(input_path, output_path):
    # Leer el PDF original
    reader = PdfReader(input_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n\n"
    
    # Configurar documento nuevo con estilos
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2.5*cm,
        rightMargin=2.5*cm,
        topMargin=2.5*cm,
        bottomMargin=2.5*cm
    )
    
    styles = setup_styles()
    story = []
    
    # Procesar el texto
    sections = re.split(r'\n\s*\n', text.strip())
    for section in sections:
        if not section.strip():
            continue
            
        # Determinar el tipo de contenido
        if section.upper() == section and len(section.split()) < 5:
            # Probablemente es un título
            story.append(Paragraph(section, styles['MainTitle']))
        elif section.startswith(('•', '-', '*')):
            # Es una lista
            for item in section.split('\n'):
                if item.strip():
                    story.append(Paragraph(f"• {item.strip()[1:].strip()}", styles['Bullet']))
        else:
            # Texto normal
            story.append(Paragraph(section, styles['BodyText']))
        
        story.append(Spacer(1, 0.5*cm))
    
    # Footer branding
    footer = Paragraph(
        "@federicomagallaness | AI & Automation Specialist",
        ParagraphStyle(
            name='Footer',
            fontSize=10,
            textColor=colors.HexColor('#6c757d'),
            alignment=1
        )
    )
    story.append(footer)
    
    # Construir el documento
    doc.build(story)
    print(f"PDF mejorado generado en: {output_path}")

# Uso
input_pdf = 'c:/Users/PC/Downloads/carrusel_agente_ia.pdf'
output_pdf = 'c:/Users/PC/Downloads/carrusel_agente_ia_mejorado.pdf'

process_pdf(input_pdf, output_pdf)
