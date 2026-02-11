import streamlit as st
import google.generativeai as genai
import datetime
import re
import json
from io import BytesIO
from typing import Dict, List, Optional
import time

# File processing imports
import PyPDF2
from docx import Document

# URL extraction imports
import requests
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("⚠️ API key not configured. Please set GOOGLE_API_KEY in Streamlit secrets.")
    st.stop()

# --- LANGUAGE TRANSLATIONS ---
TRANSLATIONS = {
    "en": {
        # Page config
        "page_title": "Cover Letter Pro",
        "main_header": "📄 Professional Cover Letter Builder",
        "main_subtitle": "AI-Powered • ATS-Optimized • 100% Free",
        
        # Sidebar
        "sidebar_config": "⚙️ Configuration",
        "language_label": "Language / Idioma:",
        "tone_label": "Letter Tone:",
        "tone_help": "Choose the tone that best fits the company culture",
        "length_label": "Letter Length:",
        "length_help": "Shorter letters are punchier; longer letters allow more detail",
        "emphasis_label": "🎯 Emphasis Areas",
        "emphasis_focus": "Focus on:",
        "emphasis_help": "Select areas to emphasize in your letter",
        "letters_generated": "Letters Generated",
        "support_header": "💖 Support This Project",
        "support_text": "If this tool helps you land your dream job, consider:",
        "buy_coffee": "Buy Me a Coffee",
        "support_footer": "Your support helps keep this tool free for everyone!",
        "pro_tips": "💡 Pro Tips",
        "pro_tips_content": """**For Best Results:**
- Include quantifiable achievements in your resume
- Copy the complete job description
- Select tone that matches company culture
- Review and customize the generated letter
- Use keywords from the job description""",
        
        # Tone profiles
        "tone_professional": "Professional & Formal",
        "tone_confident": "Confident & Assertive",
        "tone_friendly": "Friendly & Approachable",
        "tone_technical": "Technical & Precise",
        "tone_creative": "Creative & Dynamic",
        "tone_professional_desc": "Traditional corporate tone, suitable for established companies",
        "tone_confident_desc": "Bold and achievement-focused, emphasizing your value",
        "tone_friendly_desc": "Warm and personable, ideal for creative or startup environments",
        "tone_technical_desc": "Data-driven and detail-oriented for technical roles",
        "tone_creative_desc": "Innovative and expressive for creative industries",
        
        # Length options
        "length_concise": "Concise (200-250 words)",
        "length_standard": "Standard (300-350 words)",
        "length_detailed": "Detailed (400-500 words)",
        
        # Emphasis areas
        "emphasis_technical": "Technical Skills",
        "emphasis_leadership": "Leadership Experience",
        "emphasis_project": "Project Management",
        "emphasis_team": "Team Collaboration",
        "emphasis_problem": "Problem Solving",
        "emphasis_innovation": "Innovation",
        "emphasis_customer": "Customer Focus",
        "emphasis_results": "Results & Metrics",
        
        # Tabs
        "tab_create": "📝 Create Letter",
        "tab_history": "📚 History",
        "tab_guide": "ℹ️ Guide",
        
        # Create tab
        "step1": "Step 1️⃣: Input Your Information",
        "resume_label": "Your Resume/Experience",
        "resume_placeholder": """Paste your resume or relevant experience here...

Include:
• Work experience
• Skills
• Achievements
• Education""",
        "resume_help": "Maximum {max} characters",
        "job_label": "Job Description",
        "job_placeholder": """Paste the complete job description here...

Include:
• Role requirements
• Responsibilities
• Required skills
• Company information""",
        "job_help": "Maximum {max} characters",
        "upload_resume": "📎 Or Upload Resume (PDF/DOCX)",
        "upload_job": "📎 Or Paste Job URL",
        "url_placeholder": "https://example.com/job-posting",
        "extract_url": "🔗 Extract from URL",
        "save_draft": "💾 Save Draft",
        "draft_saved": "✅ Draft saved!",
        "approaching_limit": "⚠️ Approaching character limit",
        "characters": "characters",
        "keywords_header": "🔍 Detected Keywords from Job Description",
        "keywords_footer": "✨ These keywords will be naturally incorporated into your letter for ATS optimization",
        "step2": "Step 2️⃣: Generate Your Cover Letter",
        "generate_button": "🚀 Generate Letter",
        "generating": "✨ Crafting your personalized cover letter...",
        "letter_ready": "✅ Your cover letter is ready!",
        "generation_failed": "❌ Failed to generate letter. Please try again.",
        "output_header": "📄 Your Generated Cover Letter",
        "review_edit": "Review and edit your letter:",
        "review_help": "You can edit the generated letter directly here",
        "download_txt": "📥 Download TXT",
        "copy_clipboard": "📋 Copy to Clipboard",
        "copy_success": "✅ Letter displayed above - copy using Ctrl+C / Cmd+C",
        "generate_another": "🔄 Generate Another",
        "donate_button": "☕ Donate",
        "word_count": "📊 Word count: {count} words",
        
        # History tab
        "history_header": "📚 Generation History",
        "no_history": "💡 No letters generated yet. Create your first cover letter in the 'Create Letter' tab!",
        "history_count": "✅ You have generated {count} letter(s)",
        "history_letter": "Letter #{num} - {time} ({tone})",
        "history_content": "Content:",
        "history_download": "📥 Download",
        "history_template": "🔄 Use as Template",
        "template_loaded": "✅ Loaded to editor!",
        "clear_history": "🗑️ Clear All History",
        "history_cleared": "✅ History cleared!",
        
        # Guide tab
        "guide_header": "📖 How to Use This Tool",
        "guide_content": """### 🎯 Quick Start Guide

1. **Prepare Your Resume**: Copy your resume or relevant work experience
2. **Get Job Description**: Copy the complete job posting you're applying for
3. **Choose Settings**: Select tone, length, and emphasis areas in the sidebar
4. **Generate**: Click the generate button and wait for your personalized letter
5. **Review & Edit**: Customize the generated letter to add your personal touch
6. **Download**: Save your letter in your preferred format

### ✨ Best Practices

**Resume Input:**
- Include specific achievements with numbers (e.g., "Increased sales by 35%")
- List relevant skills and technologies
- Mention certifications and education
- Keep it concise but comprehensive

**Job Description:**
- Copy the entire job posting
- Include company information if available
- Don't edit or summarize - let the AI identify key points

**Tone Selection:**
- **Professional & Formal**: Traditional corporate environments, finance, law
- **Confident & Assertive**: Leadership roles, competitive industries
- **Friendly & Approachable**: Startups, creative agencies, casual cultures
- **Technical & Precise**: Engineering, data science, IT roles
- **Creative & Dynamic**: Marketing, design, media, creative fields

### 🔐 Privacy & Security

- Your data is processed securely through Google's Gemini API
- No personal information is stored permanently
- Generated letters are kept only in your browser session
- Clear your browser cache to remove all data

### 🚀 Pro Tips

- **Customize keywords**: Make sure the job description includes the specific keywords you want to highlight
- **Multiple versions**: Generate several versions and combine the best parts
- **Personal touch**: Always add a specific detail about why you're interested in THIS company
- **Proofread**: AI is great, but human review is essential
- **ATS optimization**: The tool naturally incorporates keywords for ATS systems

### ⚠️ Important Notes

- **Review carefully**: AI-generated content may need adjustments
- **Add specifics**: Include specific company details you've researched
- **Be authentic**: Use the generated letter as a starting point, not the final product
- **Update placeholders**: Replace [Your Name], [Date], etc. with actual information

### 📞 Need Help?

If you encounter issues:
- Check that both resume and job description are filled
- Ensure you're not exceeding character limits
- Wait at least 10 seconds between generations
- Try refreshing the page if something seems stuck""",
        
        # Errors
        "error_empty_resume": "❌ Resume cannot be empty.",
        "error_empty_job": "❌ Job description cannot be empty.",
        "error_short_resume": "❌ Resume seems too short. Please provide more details.",
        "error_short_job": "❌ Job description seems too short. Please provide more details.",
        "error_long_resume": "❌ Resume exceeds maximum length of {max} characters.",
        "error_long_job": "❌ Job description exceeds maximum length of {max} characters.",
        "error_rate_limit": "⏳ Please wait {seconds} seconds between generations to prevent abuse.",
        "error_generation": "❌ Generation failed: {error}",
        "error_quota": "⚠️ API quota exceeded. Please try again later or check your API key.",
        "error_file_read": "❌ Error reading file: {error}",
        "error_url_extract": "❌ Error extracting from URL: {error}",
        "error_invalid_url": "❌ Please enter a valid URL",
        "url_extracted": "✅ Content extracted from URL!",
        "file_extracted": "✅ Text extracted from file!",
        
        # Footer
        "footer_made": "Made with ❤️ for job seekers everywhere",
        "footer_support": "Support this project",
        "footer_powered": "Powered by Google Gemini AI • Built with Streamlit",
        
        # File upload
        "upload_success": "✅ File uploaded successfully!",
        "processing_file": "📄 Processing file...",
    },
    "es": {
        # Page config
        "page_title": "Generador de Cartas de Presentación",
        "main_header": "📄 Generador Profesional de Cartas de Presentación",
        "main_subtitle": "Impulsado por IA • Optimizado para ATS • 100% Gratis",
        
        # Sidebar
        "sidebar_config": "⚙️ Configuración",
        "language_label": "Language / Idioma:",
        "tone_label": "Tono de la Carta:",
        "tone_help": "Elige el tono que mejor se adapte a la cultura de la empresa",
        "length_label": "Longitud de la Carta:",
        "length_help": "Las cartas cortas son más directas; las largas permiten más detalle",
        "emphasis_label": "🎯 Áreas de Énfasis",
        "emphasis_focus": "Enfocarse en:",
        "emphasis_help": "Selecciona las áreas a enfatizar en tu carta",
        "letters_generated": "Cartas Generadas",
        "support_header": "💖 Apoya Este Proyecto",
        "support_text": "Si esta herramienta te ayuda a conseguir el trabajo de tus sueños, considera:",
        "buy_coffee": "Invítame un Café",
        "support_footer": "¡Tu apoyo ayuda a mantener esta herramienta gratuita para todos!",
        "pro_tips": "💡 Consejos Profesionales",
        "pro_tips_content": """**Para Mejores Resultados:**
- Incluye logros cuantificables en tu currículum
- Copia la descripción completa del trabajo
- Selecciona el tono que coincida con la cultura de la empresa
- Revisa y personaliza la carta generada
- Usa palabras clave de la descripción del trabajo""",
        
        # Tone profiles
        "tone_professional": "Profesional y Formal",
        "tone_confident": "Seguro y Asertivo",
        "tone_friendly": "Amigable y Cercano",
        "tone_technical": "Técnico y Preciso",
        "tone_creative": "Creativo y Dinámico",
        "tone_professional_desc": "Tono corporativo tradicional, adecuado para empresas establecidas",
        "tone_confident_desc": "Audaz y enfocado en logros, enfatizando tu valor",
        "tone_friendly_desc": "Cálido y personal, ideal para entornos creativos o startups",
        "tone_technical_desc": "Orientado a datos y detallado para roles técnicos",
        "tone_creative_desc": "Innovador y expresivo para industrias creativas",
        
        # Length options
        "length_concise": "Concisa (200-250 palabras)",
        "length_standard": "Estándar (300-350 palabras)",
        "length_detailed": "Detallada (400-500 palabras)",
        
        # Emphasis areas
        "emphasis_technical": "Habilidades Técnicas",
        "emphasis_leadership": "Experiencia en Liderazgo",
        "emphasis_project": "Gestión de Proyectos",
        "emphasis_team": "Colaboración en Equipo",
        "emphasis_problem": "Resolución de Problemas",
        "emphasis_innovation": "Innovación",
        "emphasis_customer": "Enfoque al Cliente",
        "emphasis_results": "Resultados y Métricas",
        
        # Tabs
        "tab_create": "📝 Crear Carta",
        "tab_history": "📚 Historial",
        "tab_guide": "ℹ️ Guía",
        
        # Create tab
        "step1": "Paso 1️⃣: Ingresa Tu Información",
        "resume_label": "Tu Currículum/Experiencia",
        "resume_placeholder": """Pega tu currículum o experiencia relevante aquí...

Incluye:
• Experiencia laboral
• Habilidades
• Logros
• Educación""",
        "resume_help": "Máximo {max} caracteres",
        "job_label": "Descripción del Trabajo",
        "job_placeholder": """Pega la descripción completa del trabajo aquí...

Incluye:
• Requisitos del puesto
• Responsabilidades
• Habilidades requeridas
• Información de la empresa""",
        "job_help": "Máximo {max} caracteres",
        "upload_resume": "📎 O Sube Currículum (PDF/DOCX)",
        "upload_job": "📎 O Pega URL del Trabajo",
        "url_placeholder": "https://ejemplo.com/oferta-trabajo",
        "extract_url": "🔗 Extraer de URL",
        "save_draft": "💾 Guardar Borrador",
        "draft_saved": "✅ ¡Borrador guardado!",
        "approaching_limit": "⚠️ Acercándose al límite de caracteres",
        "characters": "caracteres",
        "keywords_header": "🔍 Palabras Clave Detectadas de la Descripción del Trabajo",
        "keywords_footer": "✨ Estas palabras clave se incorporarán naturalmente en tu carta para optimización ATS",
        "step2": "Paso 2️⃣: Genera Tu Carta de Presentación",
        "generate_button": "🚀 Generar Carta",
        "generating": "✨ Creando tu carta de presentación personalizada...",
        "letter_ready": "✅ ¡Tu carta de presentación está lista!",
        "generation_failed": "❌ Error al generar la carta. Por favor, inténtalo de nuevo.",
        "output_header": "📄 Tu Carta de Presentación Generada",
        "review_edit": "Revisa y edita tu carta:",
        "review_help": "Puedes editar la carta generada directamente aquí",
        "download_txt": "📥 Descargar TXT",
        "copy_clipboard": "📋 Copiar al Portapapeles",
        "copy_success": "✅ Carta mostrada arriba - copia usando Ctrl+C / Cmd+C",
        "generate_another": "🔄 Generar Otra",
        "donate_button": "☕ Donar",
        "word_count": "📊 Conteo de palabras: {count} palabras",
        
        # History tab
        "history_header": "📚 Historial de Generación",
        "no_history": "💡 Aún no se han generado cartas. ¡Crea tu primera carta de presentación en la pestaña 'Crear Carta'!",
        "history_count": "✅ Has generado {count} carta(s)",
        "history_letter": "Carta #{num} - {time} ({tone})",
        "history_content": "Contenido:",
        "history_download": "📥 Descargar",
        "history_template": "🔄 Usar como Plantilla",
        "template_loaded": "✅ ¡Cargado en el editor!",
        "clear_history": "🗑️ Limpiar Todo el Historial",
        "history_cleared": "✅ ¡Historial limpiado!",
        
        # Guide tab
        "guide_header": "📖 Cómo Usar Esta Herramienta",
        "guide_content": """### 🎯 Guía de Inicio Rápido

1. **Prepara Tu Currículum**: Copia tu currículum o experiencia laboral relevante
2. **Obtén la Descripción del Trabajo**: Copia la oferta de trabajo completa a la que estás postulando
3. **Elige Configuración**: Selecciona tono, longitud y áreas de énfasis en la barra lateral
4. **Genera**: Haz clic en el botón de generar y espera tu carta personalizada
5. **Revisa y Edita**: Personaliza la carta generada para agregar tu toque personal
6. **Descarga**: Guarda tu carta en tu formato preferido

### ✨ Mejores Prácticas

**Entrada de Currículum:**
- Incluye logros específicos con números (ej., "Aumenté las ventas en un 35%")
- Lista habilidades y tecnologías relevantes
- Menciona certificaciones y educación
- Manténlo conciso pero completo

**Descripción del Trabajo:**
- Copia la oferta de trabajo completa
- Incluye información de la empresa si está disponible
- No edites ni resumas - deja que la IA identifique los puntos clave

**Selección de Tono:**
- **Profesional y Formal**: Entornos corporativos tradicionales, finanzas, derecho
- **Seguro y Asertivo**: Roles de liderazgo, industrias competitivas
- **Amigable y Cercano**: Startups, agencias creativas, culturas informales
- **Técnico y Preciso**: Ingeniería, ciencia de datos, roles de TI
- **Creativo y Dinámico**: Marketing, diseño, medios, campos creativos

### 🔐 Privacidad y Seguridad

- Tus datos se procesan de forma segura a través de la API de Gemini de Google
- No se almacena información personal de forma permanente
- Las cartas generadas se mantienen solo en tu sesión del navegador
- Limpia el caché de tu navegador para eliminar todos los datos

### 🚀 Consejos Profesionales

- **Personaliza palabras clave**: Asegúrate de que la descripción del trabajo incluya las palabras clave específicas que deseas resaltar
- **Múltiples versiones**: Genera varias versiones y combina las mejores partes
- **Toque personal**: Siempre agrega un detalle específico sobre por qué estás interesado en ESTA empresa
- **Revisa**: La IA es excelente, pero la revisión humana es esencial
- **Optimización ATS**: La herramienta incorpora naturalmente palabras clave para sistemas ATS

### ⚠️ Notas Importantes

- **Revisa cuidadosamente**: El contenido generado por IA puede necesitar ajustes
- **Agrega detalles**: Incluye detalles específicos de la empresa que hayas investigado
- **Sé auténtico**: Usa la carta generada como punto de partida, no como producto final
- **Actualiza marcadores**: Reemplaza [Tu Nombre], [Fecha], etc. con información real

### 📞 ¿Necesitas Ayuda?

Si encuentras problemas:
- Verifica que tanto el currículum como la descripción del trabajo estén completos
- Asegúrate de no exceder los límites de caracteres
- Espera al menos 10 segundos entre generaciones
- Intenta actualizar la página si algo parece atascado""",
        
        # Errors
        "error_empty_resume": "❌ El currículum no puede estar vacío.",
        "error_empty_job": "❌ La descripción del trabajo no puede estar vacía.",
        "error_short_resume": "❌ El currículum parece demasiado corto. Por favor, proporciona más detalles.",
        "error_short_job": "❌ La descripción del trabajo parece demasiado corta. Por favor, proporciona más detalles.",
        "error_long_resume": "❌ El currículum excede la longitud máxima de {max} caracteres.",
        "error_long_job": "❌ La descripción del trabajo excede la longitud máxima de {max} caracteres.",
        "error_rate_limit": "⏳ Por favor, espera {seconds} segundos entre generaciones para prevenir abuso.",
        "error_generation": "❌ Error en la generación: {error}",
        "error_quota": "⚠️ Cuota de API excedida. Por favor, inténtalo más tarde o verifica tu clave API.",
        "error_file_read": "❌ Error al leer archivo: {error}",
        "error_url_extract": "❌ Error al extraer de URL: {error}",
        "error_invalid_url": "❌ Por favor, ingresa una URL válida",
        "url_extracted": "✅ ¡Contenido extraído de la URL!",
        "file_extracted": "✅ ¡Texto extraído del archivo!",
        
        # Footer
        "footer_made": "Hecho con ❤️ para buscadores de empleo en todas partes",
        "footer_support": "Apoya este proyecto",
        "footer_powered": "Impulsado por Google Gemini AI • Construido con Streamlit",
        
        # File upload
        "upload_success": "✅ ¡Archivo subido exitosamente!",
        "processing_file": "📄 Procesando archivo...",
    }
}

def t(key: str, **kwargs) -> str:
    """Get translated text based on current language."""
    lang = st.session_state.get('language', 'en')
    text = TRANSLATIONS[lang].get(key, key)
    if kwargs:
        text = text.format(**kwargs)
    return text

# --- PAGE CONFIG ---
st.set_page_config(
    page_title=t("page_title"),
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stat-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        border-left: 4px solid #667eea;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3rem;
        font-weight: 600;
    }
    .copy-button {
        background-color: #28a745;
        color: white;
    }
    .keyword-badge {
        display: inline-block;
        background-color: #667eea;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        margin: 0.25rem;
        font-size: 0.85rem;
    }
    .counter {
        font-size: 0.85rem;
        color: #666;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# --- CONSTANTS ---
DONATION_LINK = "https://www.buymeacoffee.com/coverletter"
MAX_RESUME_CHARS = 5000
MAX_JOB_CHARS = 5000
RATE_LIMIT_SECONDS = 10

# --- TONE CONFIGURATIONS ---
def get_tone_profiles():
    """Get tone profiles with translations."""
    return {
        t("tone_professional"): {
            "description": t("tone_professional_desc"),
            "prompt_modifier": "formal, corporate, traditional business language"
        },
        t("tone_confident"): {
            "description": t("tone_confident_desc"),
            "prompt_modifier": "confident, assertive, achievement-oriented, emphasizing unique value proposition"
        },
        t("tone_friendly"): {
            "description": t("tone_friendly_desc"),
            "prompt_modifier": "friendly, approachable, conversational yet professional"
        },
        t("tone_technical"): {
            "description": t("tone_technical_desc"),
            "prompt_modifier": "technical, precise, data-driven, highlighting specific skills and technologies"
        },
        t("tone_creative"): {
            "description": t("tone_creative_desc"),
            "prompt_modifier": "creative, dynamic, innovative, showcasing creative thinking"
        }
    }

# --- LETTER LENGTH OPTIONS ---
def get_length_options():
    """Get length options with translations."""
    return {
        t("length_concise"): 250,
        t("length_standard"): 350,
        t("length_detailed"): 500
    }

# --- EMPHASIS AREAS ---
def get_emphasis_areas():
    """Get emphasis areas with translations."""
    return [
        t("emphasis_technical"),
        t("emphasis_leadership"),
        t("emphasis_project"),
        t("emphasis_team"),
        t("emphasis_problem"),
        t("emphasis_innovation"),
        t("emphasis_customer"),
        t("emphasis_results")
    ]

# --- FILE PROCESSING FUNCTIONS ---

def extract_text_from_pdf(file) -> str:
    """Extract text from PDF file."""
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        raise Exception(f"PDF processing error: {str(e)}")

def extract_text_from_docx(file) -> str:
    """Extract text from DOCX file."""
    try:
        doc = Document(file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        raise Exception(f"DOCX processing error: {str(e)}")

def extract_text_from_file(uploaded_file) -> str:
    """Extract text from uploaded file based on type."""
    if uploaded_file is None:
        return ""
    
    file_extension = uploaded_file.name.split('.')[-1].lower()
    
    if file_extension == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif file_extension in ['docx', 'doc']:
        return extract_text_from_docx(uploaded_file)
    else:
        raise Exception(f"Unsupported file type: {file_extension}")

# --- URL EXTRACTION FUNCTIONS ---

def extract_job_from_url(url: str) -> str:
    """Extract job posting content from URL."""
    try:
        # Validate URL
        if not url or not url.startswith(('http://', 'https://')):
            raise Exception("Invalid URL format")
        
        # Set headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Fetch the page
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        
        # Try to find common job posting containers
        job_content = None
        
        # Common class names for job postings
        job_selectors = [
            'job-description',
            'job-details',
            'job-posting',
            'job-content',
            'description',
            'posting-description',
            'job_description',
            'jobDescription'
        ]
        
        for selector in job_selectors:
            job_content = soup.find(class_=re.compile(selector, re.IGNORECASE))
            if job_content:
                break
        
        # If no specific container found, get main content
        if not job_content:
            job_content = soup.find('main') or soup.find('article') or soup.find('body')
        
        # Extract text
        if job_content:
            text = job_content.get_text(separator='\n', strip=True)
            # Clean up extra whitespace
            text = re.sub(r'\n\s*\n', '\n\n', text)
            return text
        else:
            raise Exception("Could not find job posting content on page")
            
    except requests.exceptions.Timeout:
        raise Exception("Request timed out. Please try again.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch URL: {str(e)}")
    except Exception as e:
        raise Exception(str(e))

# --- HELPER FUNCTIONS ---

def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent injection attacks."""
    if not text:
        return ""
    # Remove potentially harmful characters while preserving formatting
    text = re.sub(r'[<>{}]', '', text)
    return text.strip()

def extract_keywords(text: str, top_n: int = 10) -> List[str]:
    """Extract important keywords from job description."""
    if not text:
        return []
    
    # Simple keyword extraction (can be enhanced with NLP libraries)
    words = re.findall(r'\b[a-zA-ZáéíóúñÁÉÍÓÚÑ]{4,}\b', text.lower())
    
    # Common words to exclude (English and Spanish)
    stop_words = {
        'that', 'this', 'with', 'from', 'have', 'will', 'your',
        'their', 'would', 'about', 'which', 'there', 'other',
        'para', 'este', 'esta', 'desde', 'tener', 'será', 'tuyo',
        'suyo', 'sería', 'sobre', 'cual', 'allí', 'otro', 'otra'
    }
    
    # Filter and count
    word_freq = {}
    for word in words:
        if word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Return top keywords
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words[:top_n]]

def validate_inputs(resume: str, job: str) -> tuple[bool, str]:
    """Validate user inputs."""
    if not resume or not resume.strip():
        return False, t("error_empty_resume")
    if not job or not job.strip():
        return False, t("error_empty_job")
    if len(resume) < 100:
        return False, t("error_short_resume")
    if len(job) < 50:
        return False, t("error_short_job")
    if len(resume) > MAX_RESUME_CHARS:
        return False, t("error_long_resume", max=MAX_RESUME_CHARS)
    if len(job) > MAX_JOB_CHARS:
        return False, t("error_long_job", max=MAX_JOB_CHARS)
    return True, ""

def create_enhanced_prompt(resume: str, job: str, tone: str, length: int, 
                          keywords: List[str], emphasis_areas: List[str], language: str) -> str:
    """Create an enhanced, structured prompt for better AI generation."""
    
    tone_profiles = get_tone_profiles()
    tone_config = tone_profiles[tone]
    emphasis = ", ".join(emphasis_areas) if emphasis_areas else ("overall fit" if language == "en" else "ajuste general")
    
    language_instruction = "in English" if language == "en" else "en español"
    
    prompt = f"""You are a professional cover letter writer with expertise in ATS optimization and recruitment.

TASK: Write a compelling, personalized cover letter that will pass ATS systems and impress hiring managers.

IMPORTANT: Write the entire cover letter {language_instruction}.

TONE & STYLE: {tone_config['prompt_modifier']}

TARGET LENGTH: Approximately {length} words

STRUCTURE REQUIREMENTS:
1. Opening Paragraph: Strong hook mentioning the specific role and company, expressing genuine enthusiasm
2. Body Paragraphs (2-3): 
   - Highlight relevant experiences and achievements from the resume
   - Connect skills directly to job requirements
   - Use specific examples and quantifiable results where possible
   - Naturally incorporate these key terms from the job description: {', '.join(keywords[:5])}
3. Closing Paragraph: Call to action, expressing eagerness for an interview
4. Professional sign-off

EMPHASIS AREAS: Focus particularly on {emphasis}

FORMATTING:
- Use proper business letter format
- Include [Your Name], [Your Email], [Your Phone] placeholders at the top
- Use [Date] placeholder for the date
- Include [Hiring Manager's Name/Hiring Team] and [Company Name] placeholders
- Clear paragraph breaks for readability

KEY REQUIREMENTS:
- Make it ATS-friendly by naturally incorporating relevant keywords
- Avoid clichés and generic phrases
- Show personality while maintaining professionalism
- Demonstrate research about the company (use details from job description)
- Be specific about relevant achievements
- Avoid simply repeating the resume

CANDIDATE'S RESUME:
{resume}

JOB DESCRIPTION:
{job}

Generate the cover letter now {language_instruction}:"""
    
    return prompt

def check_rate_limit() -> bool:
    """Simple rate limiting check."""
    if 'last_generation_time' not in st.session_state:
        st.session_state.last_generation_time = 0
    
    time_since_last = time.time() - st.session_state.last_generation_time
    
    if time_since_last < RATE_LIMIT_SECONDS:
        return False
    
    st.session_state.last_generation_time = time.time()
    return True

def generate_cover_letter(resume: str, job: str, tone: str, length: int,
                         emphasis_areas: List[str], language: str) -> Optional[str]:
    """Generate cover letter using AI with error handling."""
    try:
        # Extract keywords
        keywords = extract_keywords(job)
        
        # Create enhanced prompt
        prompt = create_enhanced_prompt(resume, job, tone, length, keywords, emphasis_areas, language)
        
        # Generate with retry logic
        max_retries = 3
        for attempt in range(max_retries):
            try:
                model = genai.GenerativeModel('gemini-flash-latest')
                response = model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.7,
                        top_p=0.9,
                        top_k=40,
                        max_output_tokens=2048,
                    )
                )
                
                if response and response.text:
                    return response.text
                    
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff
        
        return None
        
    except Exception as e:
        st.error(t("error_generation", error=str(e)))
        if "quota" in str(e).lower():
            st.error(t("error_quota"))
        return None

def create_txt_download(content: str) -> BytesIO:
    """Create downloadable TXT file."""
    buffer = BytesIO()
    buffer.write(content.encode('utf-8'))
    buffer.seek(0)
    return buffer

# --- SESSION STATE INITIALIZATION ---
if 'generated_letters' not in st.session_state:
    st.session_state.generated_letters = []
if 'current_letter' not in st.session_state:
    st.session_state.current_letter = None
if 'draft_resume' not in st.session_state:
    st.session_state.draft_resume = ""
if 'draft_job' not in st.session_state:
    st.session_state.draft_job = ""
if 'language' not in st.session_state:
    st.session_state.language = 'en'

# --- HEADER ---
st.markdown(f"""
<div class="main-header">
    <h1>{t("main_header")}</h1>
    <p style="font-size: 1.1rem; margin: 0;">{t("main_subtitle")}</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header(t("sidebar_config"))
    
    # Language selection
    language_options = ["English", "Español"]
    current_lang_index = 0 if st.session_state.language == 'en' else 1
    selected_language = st.selectbox(
        t("language_label"),
        options=language_options,
        index=current_lang_index
    )
    
    # Update language in session state
    new_lang = 'en' if selected_language == "English" else 'es'
    if new_lang != st.session_state.language:
        st.session_state.language = new_lang
        st.rerun()
    
    # Tone selection with descriptions
    tone_profiles = get_tone_profiles()
    selected_tone = st.selectbox(
        t("tone_label"),
        options=list(tone_profiles.keys()),
        help=t("tone_help")
    )
    st.caption(f"💡 {tone_profiles[selected_tone]['description']}")
    
    # Length selection
    length_options = get_length_options()
    selected_length_label = st.selectbox(
        t("length_label"),
        options=list(length_options.keys()),
        help=t("length_help")
    )
    selected_length = length_options[selected_length_label]
    
    # Emphasis areas
    st.subheader(t("emphasis_label"))
    emphasis_options = get_emphasis_areas()
    emphasis_areas = st.multiselect(
        t("emphasis_focus"),
        emphasis_options,
        default=[emphasis_options[0]],
        help=t("emphasis_help")
    )
    
    st.divider()
    
    # Statistics
    if st.session_state.generated_letters:
        st.metric(t("letters_generated"), len(st.session_state.generated_letters))
    
    st.divider()
    
    # Support section
    st.subheader(t("support_header"))
    st.markdown(f"""
    {t("support_text")}
    
    ☕ [**{t("buy_coffee")}**]({DONATION_LINK})
    
    {t("support_footer")}
    """)
    
    st.divider()
    
    # Quick tips
    with st.expander(t("pro_tips")):
        st.markdown(t("pro_tips_content"))

# --- MAIN CONTENT ---
tab1, tab2, tab3 = st.tabs([t("tab_create"), t("tab_history"), t("tab_guide")])

with tab1:
    st.subheader(t("step1"))
    
    col1, col2 = st.columns(2)
    
    with col1:
        resume_input = st.text_area(
            t("resume_label"),
            value=st.session_state.draft_resume,
            height=300,
            placeholder=t("resume_placeholder"),
            help=t("resume_help", max=MAX_RESUME_CHARS)
        )
        resume_char_count = len(resume_input)
        st.markdown(f'<div class="counter">{resume_char_count}/{MAX_RESUME_CHARS} {t("characters")}</div>', 
                   unsafe_allow_html=True)
        
        if resume_char_count > MAX_RESUME_CHARS * 0.9:
            st.warning(t("approaching_limit"))
        
        # File upload for resume
        uploaded_resume = st.file_uploader(
            t("upload_resume"),
            type=['pdf', 'docx'],
            key="resume_uploader"
        )
        
        if uploaded_resume is not None:
            try:
                with st.spinner(t("processing_file")):
                    extracted_text = extract_text_from_file(uploaded_resume)
                    if extracted_text:
                        st.session_state.draft_resume = extracted_text
                        resume_input = extracted_text
                        st.success(t("file_extracted"))
                        st.rerun()
            except Exception as e:
                st.error(t("error_file_read", error=str(e)))
    
    with col2:
        job_input = st.text_area(
            t("job_label"),
            value=st.session_state.draft_job,
            height=300,
            placeholder=t("job_placeholder"),
            help=t("job_help", max=MAX_JOB_CHARS)
        )
        job_char_count = len(job_input)
        st.markdown(f'<div class="counter">{job_char_count}/{MAX_JOB_CHARS} {t("characters")}</div>', 
                   unsafe_allow_html=True)
        
        if job_char_count > MAX_JOB_CHARS * 0.9:
            st.warning(t("approaching_limit"))
        
        # URL extraction for job description
        st.markdown(f"**{t('upload_job')}**")
        url_col1, url_col2 = st.columns([3, 1])
        with url_col1:
            job_url = st.text_input(
                "URL",
                placeholder=t("url_placeholder"),
                label_visibility="collapsed"
            )
        with url_col2:
            extract_button = st.button(t("extract_url"), use_container_width=True)
        
        if extract_button and job_url:
            try:
                with st.spinner(t("processing_file")):
                    extracted_content = extract_job_from_url(job_url)
                    if extracted_content:
                        st.session_state.draft_job = extracted_content
                        job_input = extracted_content
                        st.success(t("url_extracted"))
                        st.rerun()
            except Exception as e:
                st.error(t("error_url_extract", error=str(e)))
    
    # Save draft button
    col_draft1, col_draft2 = st.columns([1, 5])
    with col_draft1:
        if st.button(t("save_draft")):
            st.session_state.draft_resume = resume_input
            st.session_state.draft_job = job_input
            st.success(t("draft_saved"))
    
    st.divider()
    
    # Keyword preview
    if job_input:
        with st.expander(t("keywords_header")):
            keywords = extract_keywords(job_input, 15)
            if keywords:
                keyword_html = "".join([f'<span class="keyword-badge">{k}</span>' for k in keywords])
                st.markdown(keyword_html, unsafe_allow_html=True)
                st.caption(t("keywords_footer"))
    
    st.divider()
    st.subheader(t("step2"))
    
    # Generate button
    col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 2])
    with col_btn2:
        generate_clicked = st.button(t("generate_button"), type="primary", use_container_width=True)
    
    if generate_clicked:
        # Sanitize inputs
        resume_clean = sanitize_input(resume_input)
        job_clean = sanitize_input(job_input)
        
        # Validate
        is_valid, error_msg = validate_inputs(resume_clean, job_clean)
        
        if not is_valid:
            st.error(error_msg)
        elif not check_rate_limit():
            st.warning(t("error_rate_limit", seconds=RATE_LIMIT_SECONDS))
        else:
            # Log generation event
            print(f"[{datetime.datetime.now()}] 💰 Letter generated - Tone: {selected_tone}, Length: {selected_length}, Language: {st.session_state.language}")
            
            # Generate with progress
            with st.spinner(t("generating")):
                progress_bar = st.progress(0)
                progress_bar.progress(25)
                
                result = generate_cover_letter(
                    resume_clean,
                    job_clean,
                    selected_tone,
                    selected_length,
                    emphasis_areas,
                    st.session_state.language
                )
                
                progress_bar.progress(100)
                
                if result:
                    st.session_state.current_letter = result
                    st.session_state.generated_letters.append({
                        'content': result,
                        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'tone': selected_tone,
                        'length': selected_length_label,
                        'language': st.session_state.language
                    })
                    st.success(t("letter_ready"))
                else:
                    st.error(t("generation_failed"))
    
    # Display current letter
    if st.session_state.current_letter:
        st.divider()
        st.subheader(t("output_header"))
        
        # Editable text area
        edited_letter = st.text_area(
            t("review_edit"),
            value=st.session_state.current_letter,
            height=500,
            help=t("review_help")
        )
        
        # Update session state if edited
        if edited_letter != st.session_state.current_letter:
            st.session_state.current_letter = edited_letter
        
        # Action buttons
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.download_button(
                label=t("download_txt"),
                data=create_txt_download(st.session_state.current_letter),
                file_name=f"cover_letter_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        with col2:
            # Copy to clipboard button (uses Streamlit's built-in functionality)
            if st.button(t("copy_clipboard"), use_container_width=True):
                st.code(st.session_state.current_letter, language=None)
                st.success(t("copy_success"))
        
        with col3:
            if st.button(t("generate_another"), use_container_width=True):
                st.session_state.current_letter = None
                st.rerun()
        
        with col4:
            st.markdown(f'<a href="{DONATION_LINK}" target="_blank"><button style="width:100%; padding:0.5rem; background-color:#FFDD00; border:none; border-radius:8px; cursor:pointer; font-weight:600;">{t("donate_button")}</button></a>', 
                       unsafe_allow_html=True)
        
        # Word count
        word_count = len(st.session_state.current_letter.split())
        st.caption(t("word_count", count=word_count))

with tab2:
    st.subheader(t("history_header"))
    
    if not st.session_state.generated_letters:
        st.info(t("no_history"))
    else:
        st.success(t("history_count", count=len(st.session_state.generated_letters)))
        
        for idx, letter in enumerate(reversed(st.session_state.generated_letters)):
            letter_lang = letter.get('language', 'en')
            lang_display = "🇬🇧 EN" if letter_lang == 'en' else "🇪🇸 ES"
            with st.expander(f"{t('history_letter', num=len(st.session_state.generated_letters) - idx, time=letter['timestamp'], tone=letter['tone'])} - {lang_display}"):
                st.text_area(
                    t("history_content"),
                    value=letter['content'],
                    height=300,
                    key=f"history_{idx}",
                    disabled=True
                )
                
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label=t("history_download"),
                        data=create_txt_download(letter['content']),
                        file_name=f"cover_letter_{letter['timestamp'].replace(':', '-').replace(' ', '_')}.txt",
                        mime="text/plain",
                        key=f"download_btn_{idx}",
                        use_container_width=True
                    )
                with col2:
                    if st.button(t("history_template"), key=f"template_{idx}", use_container_width=True):
                        st.session_state.current_letter = letter['content']
                        st.success(t("template_loaded"))
                        st.rerun()
        
        # Clear history button
        st.divider()
        if st.button(t("clear_history"), type="secondary"):
            st.session_state.generated_letters = []
            st.success(t("history_cleared"))
            st.rerun()

with tab3:
    st.subheader(t("guide_header"))
    st.markdown(t("guide_content"))

# --- FOOTER ---
st.divider()
st.markdown(f"""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>{t("footer_made")} | <a href="{DONATION_LINK}" target="_blank">{t("footer_support")}</a></p>
    <p style="font-size: 0.85rem;">{t("footer_powered")}</p>
</div>
""", unsafe_allow_html=True)
