from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.units import inch
from datetime import datetime

# Configuración
pdf_filename = "agente_ia_instagram.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                        rightMargin=36, leftMargin=36,
                        topMargin=36, bottomMargin=36)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='SlideTitle', 
                        fontSize=30, 
                        leading=35,
                        fontName='Helvetica-Bold',
                        textColor=colors.black,
                        spaceAfter=15))

styles.add(ParagraphStyle(name='SlideSubtitle', 
                        fontSize=22, 
                        leading=28,
                        fontName='Helvetica',
                        textColor=colors.purple,
                        spaceAfter=20))

styles.add(ParagraphStyle(name='BodyText', 
                        fontSize=16,
                        leading=22,
                        fontName='Helvetica',
                        textColor=colors.darkgrey,
                        spaceAfter=15))

styles.add(ParagraphStyle(name='Highlight', 
                        fontSize=18,
                        leading=24,
                        fontName='Helvetica-Bold',
                        textColor=colors.black,
                        spaceAfter=20))

# Contenido de los slides
story = []

# Slide 1
story.append(Paragraph("Tu nuevo empleado no duerme, no cobra sueldo y nunca se equivoca.", styles["SlideTitle"]))
story.append(Paragraph("¿Cómo funciona realmente un Agente de IA?", styles["SlideSubtitle"]))
story.append(Spacer(1, 20))
story.append(Image('WhatsApp Image 2026-04-21 at 5.12.39 PM.jpeg', width=5*inch, height=3.5*inch))
story.append(PageBreak())

# Slide 2
bullets2 = [
    "Pasar datos de A a B manualmente",
    "Responder las mismas dudas básicas por WhatsApp",
    "Mover leads de Excel a CRM",
]
story.append(Paragraph("El 90% de los negocios están estancados en el 'trabajo operativo'", styles["SlideTitle"]))
story.extend([Paragraph(f"• {item}", styles["BodyText"]) for item in bullets2])
story.append(Spacer(1, 20))
story.append(Paragraph('"Hacer esto no es crecer. Es simplemente sobrevivir."', styles["Highlight"]))
story.append(PageBreak())

# Slide 3
story.append(Paragraph("Chatbot vs. Agente de IA. No son lo mismo.", styles["SlideTitle"]))
story.append(Paragraph("<b>Chatbot:</b> Es reactivo. Sigue un árbol de decisiones rígido (A, B, C).", styles["BodyText"]))
story.append(Paragraph("<b>Agente:</b> Es proactivo. Utiliza un modelo de lenguaje (LLM) para razonar y decidir.", styles["BodyText"]))
story.append(PageBreak())

# Slide 4
bullets4 = [
    "Cerebro (LLM): Entiende lenguaje natural en contexto",
    "Manos (APIs): Conecta a Gmail, CRM, WhatsApp (vía n8n)",
    "Memoria: Registra interacciones previas",
]
story.append(Paragraph("Así es como se estructuran", styles["SlideTitle"]))
story.extend([Paragraph(f"• {item}", styles["BodyText"]) for item in bullets4])
story.append(PageBreak())

# Slide 5
flow = [
    "Input: Consulta por WhatsApp",
    "Razonamiento: IA detecta intención ('agendar')",
    "Acción: Usa API de Google Calendar",
    "Confirmación: 'Turno reservado para mañana a las 10am'",
]
story.append(Paragraph("¿Cómo actúan? Un flujo simple:", styles["SlideTitle"]))
story.extend([Paragraph(f"{i+1}. {item}", styles["BodyText"]) for i, item in enumerate(flow)])
story.append(PageBreak())

# Slide 6
story.append(Paragraph("Dejá de ser el cuello de botella de tu propia operación", styles["SlideTitle"]))
story.append(Paragraph('"La automatización con Agentes de IA ya no es el futuro, es el estándar operativo de hoy."', styles["Highlight"]))
story.append(Spacer(1, 30))
story.append(Image('WhatsApp Image 2026-04-21 at 5.12.39 PM.jpeg', width=5*inch, height=3.5*inch))
story.append(Spacer(1, 30))
story.append(Paragraph("Comentá 'AGENTE' y te cuento cómo empezar a delegar", styles["SlideSubtitle"]))

# Footer branding
footer = Paragraph("@federicomagallaness | AI & Automation Specialist", styles["BodyText"])

# Construir documento
doc.build(story)

print(f"PDF generado exitosamente: {pdf_filename}")
