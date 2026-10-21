"""Build concise public CVs from the professional scope used by this portfolio."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parents[1]
fontroot=Path('/usr/share/fonts/truetype/dejavu')
pdfmetrics.registerFont(TTFont('CV',str(fontroot/'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('CVBold',str(fontroot/'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFontFamily('CV',normal='CV',bold='CVBold',italic='CV',boldItalic='CVBold')
styles={
'name':ParagraphStyle('name',fontName='CVBold',fontSize=27,leading=33,textColor=colors.HexColor('#1d2b1a'),spaceAfter=9),
'role':ParagraphStyle('role',fontName='CVBold',fontSize=11,leading=16,textColor=colors.HexColor('#41523b'),spaceAfter=10),
'body':ParagraphStyle('body',fontName='CV',fontSize=9,leading=14,spaceAfter=8,textColor=colors.HexColor('#30382d')),
'heading':ParagraphStyle('heading',fontName='CVBold',fontSize=11,leading=16,spaceBefore=14,spaceAfter=9,textColor=colors.HexColor('#41523b')),
'small':ParagraphStyle('small',fontName='CV',fontSize=8,leading=12,textColor=colors.HexColor('#52594f'),spaceAfter=6)}
for lang in ['ES','EN']:
 es=lang=='ES'
 def t(a,b):return a if es else b
 out=ROOT/'assets/downloads'/f'Nicolas_Alderete_CV_{lang}.pdf'
 doc=SimpleDocTemplate(str(out),pagesize=(595.28,841.89),rightMargin=48,leftMargin=48,topMargin=42,bottomMargin=40,title='Nicolás Alderete | Operations Analytics & Reporting',author='Nicolás Alderete')
 items=[]
 def p(s,k='body'):items.append(Paragraph(s,styles[k]))
 p('Nicolás Alderete','name')
 p(t('Supervisor de Customer Service | Operations Reporting Analyst','Customer Service Supervisor | Operations Reporting Analyst'),'role')
 p('Buenos Aires, Argentina','small')
 p('<link href="https://nicoalderete.github.io/">nicoalderete.github.io</link> · <link href="https://www.linkedin.com/in/nicolas-alderete/">LinkedIn</link> · <link href="https://github.com/Nicoalderete">GitHub</link>','small')
 p(t('PERFIL','PROFILE'),'heading')
 p(t('Combino supervisión operativa de Customer Service con análisis de datos, reporting y automatización. Desarrollo reportes, dashboards y herramientas de seguimiento para organizar información, dar visibilidad al desempeño y acompañar decisiones de gestión.','I combine operational Customer Service supervision with data analytics, reporting and automation. I develop reports, dashboards and tracking tools to organise information, make performance visible and support management decisions.'))
 p(t('EXPERIENCIA','EXPERIENCE'),'heading')
 p('<b>deRentas Carsharing</b> · '+t('Marzo 2025 - Actualidad','March 2025 - Present'))
 p(t('Supervisión de Customer Service y reporting operativo. Evolución desde supervisión de operaciones de flota hacia una función con foco en indicadores y análisis.','Customer Service supervision and operational reporting. Progression from fleet operations supervision towards a role focused on metrics and analytics.'))
 for s in t([
 'Preparación y revisión de reportes periódicos de bajas: clasificación de motivos, segmentación y comunicación de hallazgos.',
 'Seguimiento de indicadores de clientes y operación, con definición de cortes, criterios de cálculo y prioridades de revisión.',
 'Desarrollo de herramientas de control y automatización en Google Sheets y Apps Script, incluyendo programación de revisiones.',
 'Preparación de información para la supervisión y la dirección, conectando indicadores con contexto y próximos pasos.'
 ],[
 'Prepare and review recurring departure reports, including reason classification, segmentation and communication of findings.',
 'Track customer and operational metrics, defining cutoffs, calculation criteria and review priorities.',
 'Develop tracking and automation tools in Google Sheets and Apps Script, including inspection scheduling.',
 'Prepare information for supervisors and management, connecting metrics with context and next steps.'
 ]):p('• '+s)
 p(t('PROYECTOS SELECCIONADOS','SELECTED PROJECTS'),'heading')
 p(t('<b>Top 100 Airports - Python y SQL.</b> Análisis exploratorio y extensión de aprendizaje con validación de CSV, SQLite, vistas y auditoría de carga.','<b>Top 100 Airports - Python and SQL.</b> Exploratory analysis and a learning extension with CSV validation, SQLite, analytical views and load auditing.'))
 p(t('<b>Análisis comercial - Power BI y Tableau.</b> Proyectos académicos de ventas por período, producto y ciudad, con evidencia y límites documentados.','<b>Commercial analytics - Power BI and Tableau.</b> Academic sales projects by period, product and city, with documented evidence and limitations.'))
 p(t('HERRAMIENTAS','TOOLS'),'heading')
 p('Excel · Google Sheets · SQL · Python / Pandas · Power BI · DAX · Tableau · Google Apps Script · SQLite')
 p(t('FORMACIÓN','TRAINING'),'heading')
 p('IBM Data Analyst Professional Certificate. '+t('Formación en Excel, SQL, Data Analytics y Tableau en Coderhouse.','Training in Excel, SQL, Data Analytics and Tableau at Coderhouse.'))
 p(t('DESARROLLO PROFESIONAL','PROFESSIONAL DEVELOPMENT'),'heading')
 p(t('Orientación hacia Data Engineering, con interés en integración, transformación, calidad de datos y procesos reproducibles.','Developing towards Data Engineering, with an interest in integration, transformation, data quality and reproducible processes.'))
 def footer(c,d):
  c.setStrokeColor(colors.HexColor('#b3c5aa'));c.line(48,35,547,35);c.setFont('CV',7);c.setFillColor(colors.HexColor('#596352'));c.drawString(48,23,'Nicolás Alderete · Operations Analytics & Reporting');c.drawRightString(547,23,t('Octubre 2026','October 2026'))
 doc.build(items,onFirstPage=footer,onLaterPages=footer)
 print(out)
