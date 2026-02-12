"""
Translations module for CoverLetterPro
Provides multi-language support for the application interface
"""

TRANSLATIONS = {
    'en': {
        # Header & Branding
        'app_title': 'CoverLetterPro',
        'app_subtitle': 'AI-Powered Professional Cover Letter Builder',
        'app_tagline': 'ATS-Optimized • Industry Templates • Smart Matching • Professional Export',
        
        # Buttons
        'btn_theme': '🌓 Theme',
        'btn_theme_help': 'Toggle light/dark mode',
        'btn_profile': '👤 Profile',
        'btn_profile_help': 'Manage your profile',
        'btn_continue': 'Continue to {} →',
        'btn_go_to_profile': 'Go to Profile',
        'btn_generate': '🚀 Generate Cover Letter(s)',
        'btn_extract_url': '🔗 Extract from URL',
        'btn_select_version': '✅ Select This Version',
        'btn_download_pdf': '📄 Download PDF',
        'btn_download_word': '📝 Download Word',
        'btn_copy_clipboard': '📋 Copy to Clipboard',
        'btn_save_history': '💾 Save to History',
        'btn_use_template': '🔄 Use as Template',
        'btn_download': '📥 Download',
        'btn_delete': '🗑️ Delete',
        'btn_export_all': '📥 Export All as ZIP',
        'btn_clear_history': '🗑️ Clear All History',
        'btn_save_profile': '💾 Save Profile',
        'btn_apply_suggestion': 'Apply Suggestion {}',
        
        # Sidebar
        'sidebar_config': '⚙️ Configuration',
        'sidebar_profile_set': '👤 **{}**\n{}',
        'sidebar_no_profile': '👤 No profile set. Click Profile button to create one.',
        'sidebar_language': '🌐 Language',
        'sidebar_language_help': 'Select interface language',
        'sidebar_industry': '🏢 Industry',
        'sidebar_industry_help': 'Select your target industry for optimized templates',
        'sidebar_experience': '📊 Experience Level',
        'sidebar_experience_help': 'Your experience level for tone adjustment',
        'sidebar_writing_mode': '✍️ Writing Mode',
        'sidebar_writing_mode_help': 'Choose writing style that matches company culture',
        'sidebar_letter_length': '📏 Letter Length',
        'sidebar_letter_length_help': 'Adjust letter length to your needs',
        'sidebar_statistics': '📊 Statistics',
        'sidebar_letters': 'Letters',
        'sidebar_versions': 'Versions',
        'sidebar_pro_tips': '💡 Pro Tips',
        'sidebar_success_stories': '⭐ Success Stories',
        
        # Experience Levels
        'exp_entry': 'Entry Level',
        'exp_mid': 'Mid Level',
        'exp_senior': 'Senior Level',
        'exp_executive': 'Executive',
        
        # Writing Modes
        'mode_professional': 'Professional & Formal',
        'mode_confident': 'Confident & Assertive',
        'mode_creative': 'Creative & Dynamic',
        'mode_technical': 'Technical & Precise',
        'mode_friendly': 'Friendly & Approachable',
        
        # Letter Lengths
        'length_concise': 'Concise (200-250)',
        'length_standard': 'Standard (300-350)',
        'length_detailed': 'Detailed (400-500)',
        
        # Pro Tips
        'tips_title': '**For Best Results:**',
        'tips_1': '- Complete your profile first',
        'tips_2': '- Use industry-specific templates',
        'tips_3': '- Review ATS score > 80%',
        'tips_4': '- Compare A/B versions',
        'tips_5': '- Export with company branding',
        
        # Success Stories
        'story_1_quote': '*"Got 3 interviews in 1 week!"*',
        'story_1_author': '- Sarah M., Software Engineer',
        'story_2_quote': '*"ATS score went from 45% to 92%"*',
        'story_2_author': '- James T., Marketing Manager',
        'story_3_quote': '*"Professional export saved me hours"*',
        'story_3_author': '- Lisa K., Product Designer',
        
        # Progress Steps
        'progress_title': '📍 Your Progress',
        'step_profile': 'Profile',
        'step_input': 'Input',
        'step_customize': 'Customize',
        'step_generate': 'Generate',
        'step_review': 'Review & Export',
        
        # Main Tabs
        'tab_create': '📝 Create Letter',
        'tab_analysis': '🔍 Analysis & Scoring',
        'tab_history': '📚 History & Versions',
        'tab_profile': '👤 Profile & Settings',
        'tab_guide': '📖 Guide & Examples',
        
        # Tab 1: Create Letter
        'create_title': '## Step-by-Step Letter Creation',
        'create_step1_title': '### 1️⃣ Profile Information',
        'create_step1_warning': '⚠️ Please complete your profile in the \'Profile & Settings\' tab first!',
        'create_step1_success': '✅ Profile ready: {}',
        'create_step2_title': '### 2️⃣ Input Your Information',
        'create_step2_resume_label': '**📄 Your Resume/Experience**',
        'create_step2_resume_placeholder': 'Paste your resume here...\n\nInclude:\n• Work experience\n• Skills\n• Achievements\n• Education',
        'create_step2_resume_help': 'Upload or paste your complete resume',
        'create_step2_resume_upload': 'Or upload resume (PDF/DOCX)',
        'create_step2_resume_file': '📄 File: {}',
        'create_step2_resume_chars': '📊 Characters: {}',
        'create_step2_job_label': '**💼 Job Description**',
        'create_step2_job_placeholder': 'Paste job description here...\n\nInclude:\n• Requirements\n• Responsibilities\n• Skills needed\n• Company info',
        'create_step2_job_help': 'Paste the complete job posting',
        'create_step2_job_url': 'Or paste job posting URL',
        'create_step2_job_url_help': 'We\'ll extract the content automatically',
        'create_step2_extracting': 'Extracting job details...',
        'create_step2_extracted': '✅ Content extracted!',
        'create_step2_complete_msg': '💡 Complete both resume and job description to continue',
        'create_step3_title': '### 3️⃣ Customize Your Letter',
        'create_step3_template': '📋 Choose Template',
        'create_step3_template_help': 'Select an industry-specific template',
        'create_step3_preview': '👁️ Preview Template',
        'create_step3_emphasis': '**🎯 Emphasis Areas**',
        'create_step3_emphasis_help': 'Highlight specific strengths',
        'create_step3_keywords': '**🔑 Additional Keywords (Optional)**',
        'create_step3_keywords_placeholder': 'e.g., Python, Agile, Leadership, AWS',
        'create_step3_keywords_help': 'Extra keywords to emphasize',
        'create_step4_title': '### 4️⃣ Generate Your Letter',
        'create_step4_options': '**Generation Options**',
        'create_step4_num_versions': '📊 Number of Versions (A/B Testing)',
        'create_step4_num_versions_help': 'Generate multiple versions for comparison',
        'create_step4_analysis': '📈 Include AI Analysis',
        'create_step4_analysis_help': 'Get writing suggestions and effectiveness score',
        'create_step4_error': '❌ Please complete Step 2 first!',
        'create_step4_generating': '✨ Generating {} version(s)...',
        'create_step4_success': '✅ Generated {} version(s) successfully!',
        'create_step5_title': '### 5️⃣ Review & Export',
        'create_step5_ready': '✅ {} version(s) ready for review!',
        'create_step5_compare': '**📊 Compare Versions (A/B Testing)**',
        'create_step5_version': '**Version {}**',
        'create_step5_words': '📊 {} words',
        'create_step5_selected': 'Selected!',
        'create_step5_your_letter': 'Your Cover Letter',
        'create_step5_edit_help': 'You can edit the letter directly here',
        'create_step5_word_count': '📊 Word count: {} words',
        'create_step5_export_title': '### 📤 Export Options',
        'create_step5_creating_pdf': 'Creating PDF...',
        'create_step5_word_coming': 'Word export feature coming soon!',
        'create_step5_copy_msg': '✅ Use Ctrl+C to copy from the text area above',
        'create_step5_saved': '✅ Saved to history!',
        'create_step5_generate_first': '💡 Generate a letter first to see it here!',
        
        # Emphasis Areas
        'emphasis_technical': 'Technical Skills',
        'emphasis_leadership': 'Leadership',
        'emphasis_problem': 'Problem Solving',
        'emphasis_innovation': 'Innovation',
        'emphasis_team': 'Team Collaboration',
        'emphasis_project': 'Project Management',
        'emphasis_customer': 'Customer Focus',
        'emphasis_results': 'Results & Metrics',
        
        # Tab 2: Analysis & Scoring
        'analysis_title': '## 📊 AI-Powered Analysis & Scoring',
        'analysis_generate_first': '💡 Generate a cover letter first to see analysis and scoring!',
        'analysis_overall_title': '### 🎯 Overall Effectiveness Score',
        'analysis_overall_score': 'Overall Score',
        'analysis_ats_score': 'ATS Score',
        'analysis_grammar_score': 'Grammar',
        'analysis_keywords_score': 'Keywords',
        'analysis_skills_score': 'Skills Match',
        'analysis_score_label': '**Score: {}/100**',
        'analysis_strengths': '**✅ Strengths:**',
        'analysis_improvements': '**⚠️ Improvements:**',
        'analysis_ats_title': '🎯 ATS Optimization Analysis',
        'analysis_grammar_title': '✍️ Grammar & Style Analysis',
        'analysis_issues_found': '**Issues Found:**',
        'analysis_no_issues': '✅ No grammar issues detected!',
        'analysis_keywords_title': '🔑 Keyword Analysis',
        'analysis_coverage': '**Coverage: {}%**',
        'analysis_matched_keywords': '**✅ Matched Keywords:**',
        'analysis_missing_keywords': '**⚠️ Missing Keywords:**',
        'analysis_skills_title': '💼 Skills Matching Analysis',
        'analysis_match': '**Match: {}%**',
        'analysis_highlighted_skills': '**✅ Highlighted Skills:**',
        'analysis_consider_adding': '**💡 Consider Adding:**',
        'analysis_suggestions_title': '### 🤖 AI-Powered Improvement Suggestions',
        'analysis_suggestion': '💡 Suggestion {}: {}',
        'analysis_applied': '✅ Suggestion applied! Regenerate to see changes.',
        
        # Tab 3: History & Versions
        'history_title': '## 📚 History & Version Management',
        'history_empty': '💡 No saved letters yet. Generate and save your first letter!',
        'history_count': '✅ You have {} saved letter(s)',
        'history_search': '🔍 Search letters',
        'history_search_placeholder': 'Search by keywords, industry, etc.',
        'history_filter_industry': 'Filter by Industry',
        'history_filter_all': 'All',
        'history_sort': 'Sort by',
        'history_sort_newest': 'Newest',
        'history_sort_oldest': 'Oldest',
        'history_sort_score': 'Score',
        'history_letter_title': '📄 Letter #{} - {} - {}',
        'history_content': 'Content',
        'history_metadata': '**Metadata:**',
        'history_industry': 'Industry: {}',
        'history_mode': 'Mode: {}',
        'history_template': 'Template: {}',
        'history_score': 'Score',
        'history_loaded': '✅ Loaded as template!',
        'history_deleted': '✅ Deleted!',
        'history_exporting': 'Exporting all letters...',
        'history_confirm_clear': 'I\'m sure I want to delete all letters',
        'history_cleared': '✅ All history cleared!',
        
        # Tab 4: Profile & Settings
        'profile_title': '## 👤 Profile & Settings',
        'profile_personal_info': '### Personal Information',
        'profile_name': 'Full Name *',
        'profile_name_placeholder': 'John Doe',
        'profile_email': 'Email Address *',
        'profile_email_placeholder': 'john.doe@email.com',
        'profile_phone': 'Phone Number',
        'profile_phone_placeholder': '+1 (555) 123-4567',
        'profile_location': 'Location',
        'profile_location_placeholder': 'San Francisco, CA',
        'profile_linkedin': 'LinkedIn URL',
        'profile_linkedin_placeholder': 'https://linkedin.com/in/johndoe',
        'profile_portfolio': 'Portfolio/Website',
        'profile_portfolio_placeholder': 'https://johndoe.com',
        'profile_years': 'Years of Experience',
        'profile_title_field': 'Current/Recent Job Title',
        'profile_title_placeholder': 'Senior Software Engineer',
        'profile_summary': '### Professional Summary',
        'profile_summary_label': 'Brief professional summary (optional)',
        'profile_summary_placeholder': 'A brief summary of your professional background...',
        'profile_skills': '### Key Skills',
        'profile_skills_label': 'List your key skills (comma-separated)',
        'profile_skills_placeholder': 'Python, JavaScript, Project Management, Leadership',
        'profile_required_error': '❌ Name and email are required!',
        'profile_saved': '✅ Profile saved successfully!',
        'profile_settings': '### ⚙️ Application Settings',
        'profile_notifications': '🔔 Enable notifications',
        'profile_autosave': '💾 Auto-save drafts',
        'profile_analytics': '📊 Show advanced analytics',
        'profile_animations': '🎨 Enable animations',
        'profile_email_export': '📧 Email export copies',
        'profile_default_length': 'Default letter length (words)',
        
        # Tab 5: Guide & Examples
        'guide_title': '## 📖 Complete Guide & Examples',
        'guide_quick_start': 'Quick Start',
        'guide_best_practices': 'Best Practices',
        'guide_examples': 'Examples',
        'guide_ats_tips': 'ATS Tips',
        'guide_faq': 'FAQ',
        'guide_quick_start_title': '### 🚀 Quick Start Guide',
        'guide_best_practices_title': '### ✨ Best Practices',
        'guide_examples_title': '### 📚 Examples by Industry',
        'guide_ats_tips_title': '### 🎯 ATS Tips',
        'guide_faq_title': '### ❓ FAQ',
        
        # Industries
        'industry_technology': 'Technology',
        'industry_finance': 'Finance & Banking',
        'industry_healthcare': 'Healthcare & Medical',
        'industry_education': 'Education & Academia',
        'industry_marketing': 'Marketing & Advertising',
        'industry_sales': 'Sales & Business Development',
        'industry_engineering': 'Engineering & Manufacturing',
        'industry_legal': 'Legal & Compliance',
        'industry_design': 'Design & Creative',
        'industry_hospitality': 'Hospitality & Service',
        'industry_real_estate': 'Real Estate',
        'industry_consulting': 'Consulting',
        'industry_nonprofit': 'Non-Profit & Social Services',
        'industry_government': 'Government & Public Sector',
        
        # Template Previews
        'template_preview_title': '**Preview: {} Template**',
        'template_emphasizes': 'This template emphasizes:',
        'template_tone': 'Tone:',
        'template_length': 'Length:',
        'template_not_available': 'Template preview not available. This template will be customized based on your inputs.',
        
        # Scoring & Effectiveness
        'grade_a': 'A',
        'grade_b': 'B',
        'grade_c': 'C',
        'grade_d': 'D',
        'grade_f': 'F',
        'effectiveness_exceptional': 'Exceptional - Very likely to impress recruiters',
        'effectiveness_excellent': 'Excellent - Strong chance of getting interview',
        'effectiveness_good': 'Good - Competitive application',
        'effectiveness_fair': 'Fair - Needs some improvements',
        'effectiveness_needs_work': 'Needs Work - Requires significant revision',
        
        # Suggestions
        'suggestion_ats_title': 'Improve ATS Compatibility',
        'suggestion_ats_desc': 'Your letter may not pass automated screening. Add more keywords from the job description and use standard formatting.',
        'suggestion_ats_example': 'Review the job posting and naturally incorporate key terms like required skills, qualifications, and technologies.',
        'suggestion_grammar_title': 'Fix Grammar and Style Issues',
        'suggestion_grammar_desc': 'There are grammar or style issues that could hurt your credibility. Review and correct them.',
        'suggestion_grammar_example': 'Use our grammar checker to identify and fix specific issues.',
        'suggestion_keywords_title': 'Add More Relevant Keywords',
        'suggestion_keywords_desc': 'Your letter is missing important keywords from the job description.',
        'suggestion_keywords_example': 'Review the "Missing Keywords" section and naturally incorporate them into your letter.',
        'suggestion_structure_title': 'Improve Letter Structure',
        'suggestion_structure_desc': 'Your letter structure could be clearer. Use 3-4 distinct paragraphs.',
        'suggestion_structure_example': 'Paragraph 1: Opening with enthusiasm\nParagraph 2-3: Relevant experience and achievements\nParagraph 4: Strong closing with call to action',
        'suggestion_personal_title': 'Make It More Personal and Specific',
        'suggestion_personal_desc': 'Your letter feels generic. Add specific details about the company and role.',
        'suggestion_personal_example': 'Research the company and mention: specific products/projects, company values, recent news, or why you\'re excited about THIS role at THIS company.',
        'suggestion_quantify_title': 'Add Quantifiable Achievements',
        'suggestion_quantify_desc': 'Include specific numbers, percentages, or metrics to demonstrate impact.',
        'suggestion_quantify_example': 'Instead of "improved performance", say "improved performance by 35%" or "led team of 8 engineers"',
        'suggestion_active_title': 'Use More Active Voice',
        'suggestion_active_desc': 'Found {} instances of passive voice. Active voice is more engaging.',
        'suggestion_active_example': 'Change "The project was completed by me" to "I completed the project"',
        
        # Common Messages
        'msg_loading': 'Loading...',
        'msg_success': 'Success!',
        'msg_error': 'Error',
        'msg_warning': 'Warning',
        'msg_info': 'Information',
    },
    
    'es': {
        # Header & Branding
        'app_title': 'CoverLetterPro',
        'app_subtitle': 'Constructor Profesional de Cartas de Presentación con IA',
        'app_tagline': 'Optimizado para ATS • Plantillas Industriales • Coincidencia Inteligente • Exportación Profesional',
        
        # Buttons
        'btn_theme': '🌓 Tema',
        'btn_theme_help': 'Cambiar modo claro/oscuro',
        'btn_profile': '👤 Perfil',
        'btn_profile_help': 'Administrar tu perfil',
        'btn_continue': 'Continuar a {} →',
        'btn_go_to_profile': 'Ir al Perfil',
        'btn_generate': '🚀 Generar Carta(s) de Presentación',
        'btn_extract_url': '🔗 Extraer de URL',
        'btn_select_version': '✅ Seleccionar Esta Versión',
        'btn_download_pdf': '📄 Descargar PDF',
        'btn_download_word': '📝 Descargar Word',
        'btn_copy_clipboard': '📋 Copiar al Portapapeles',
        'btn_save_history': '💾 Guardar en Historial',
        'btn_use_template': '🔄 Usar como Plantilla',
        'btn_download': '📥 Descargar',
        'btn_delete': '🗑️ Eliminar',
        'btn_export_all': '📥 Exportar Todo como ZIP',
        'btn_clear_history': '🗑️ Borrar Todo el Historial',
        'btn_save_profile': '💾 Guardar Perfil',
        'btn_apply_suggestion': 'Aplicar Sugerencia {}',
        
        # Sidebar
        'sidebar_config': '⚙️ Configuración',
        'sidebar_profile_set': '👤 **{}**\n{}',
        'sidebar_no_profile': '👤 No hay perfil configurado. Haz clic en el botón Perfil para crear uno.',
        'sidebar_language': '🌐 Idioma',
        'sidebar_language_help': 'Seleccionar idioma de la interfaz',
        'sidebar_industry': '🏢 Industria',
        'sidebar_industry_help': 'Selecciona tu industria objetivo para plantillas optimizadas',
        'sidebar_experience': '📊 Nivel de Experiencia',
        'sidebar_experience_help': 'Tu nivel de experiencia para ajuste de tono',
        'sidebar_writing_mode': '✍️ Modo de Escritura',
        'sidebar_writing_mode_help': 'Elige el estilo de escritura que coincida con la cultura de la empresa',
        'sidebar_letter_length': '📏 Longitud de la Carta',
        'sidebar_letter_length_help': 'Ajusta la longitud de la carta según tus necesidades',
        'sidebar_statistics': '📊 Estadísticas',
        'sidebar_letters': 'Cartas',
        'sidebar_versions': 'Versiones',
        'sidebar_pro_tips': '💡 Consejos Profesionales',
        'sidebar_success_stories': '⭐ Historias de Éxito',
        
        # Experience Levels
        'exp_entry': 'Nivel de Entrada',
        'exp_mid': 'Nivel Medio',
        'exp_senior': 'Nivel Senior',
        'exp_executive': 'Ejecutivo',
        
        # Writing Modes
        'mode_professional': 'Profesional y Formal',
        'mode_confident': 'Seguro y Asertivo',
        'mode_creative': 'Creativo y Dinámico',
        'mode_technical': 'Técnico y Preciso',
        'mode_friendly': 'Amigable y Cercano',
        
        # Letter Lengths
        'length_concise': 'Concisa (200-250)',
        'length_standard': 'Estándar (300-350)',
        'length_detailed': 'Detallada (400-500)',
        
        # Pro Tips
        'tips_title': '**Para Mejores Resultados:**',
        'tips_1': '- Completa tu perfil primero',
        'tips_2': '- Usa plantillas específicas de la industria',
        'tips_3': '- Revisa puntuación ATS > 80%',
        'tips_4': '- Compara versiones A/B',
        'tips_5': '- Exporta con marca de la empresa',
        
        # Success Stories
        'story_1_quote': '*"¡Conseguí 3 entrevistas en 1 semana!"*',
        'story_1_author': '- Sarah M., Ingeniera de Software',
        'story_2_quote': '*"La puntuación ATS pasó de 45% a 92%"*',
        'story_2_author': '- James T., Gerente de Marketing',
        'story_3_quote': '*"La exportación profesional me ahorró horas"*',
        'story_3_author': '- Lisa K., Diseñadora de Productos',
        
        # Progress Steps
        'progress_title': '📍 Tu Progreso',
        'step_profile': 'Perfil',
        'step_input': 'Entrada',
        'step_customize': 'Personalizar',
        'step_generate': 'Generar',
        'step_review': 'Revisar y Exportar',
        
        # Main Tabs
        'tab_create': '📝 Crear Carta',
        'tab_analysis': '🔍 Análisis y Puntuación',
        'tab_history': '📚 Historial y Versiones',
        'tab_profile': '👤 Perfil y Configuración',
        'tab_guide': '📖 Guía y Ejemplos',
        
        # Tab 1: Create Letter
        'create_title': '## Creación de Carta Paso a Paso',
        'create_step1_title': '### 1️⃣ Información del Perfil',
        'create_step1_warning': '⚠️ ¡Por favor completa tu perfil en la pestaña \'Perfil y Configuración\' primero!',
        'create_step1_success': '✅ Perfil listo: {}',
        'create_step2_title': '### 2️⃣ Ingresa Tu Información',
        'create_step2_resume_label': '**📄 Tu Currículum/Experiencia**',
        'create_step2_resume_placeholder': 'Pega tu currículum aquí...\n\nIncluye:\n• Experiencia laboral\n• Habilidades\n• Logros\n• Educación',
        'create_step2_resume_help': 'Carga o pega tu currículum completo',
        'create_step2_resume_upload': 'O sube tu currículum (PDF/DOCX)',
        'create_step2_resume_file': '📄 Archivo: {}',
        'create_step2_resume_chars': '📊 Caracteres: {}',
        'create_step2_job_label': '**💼 Descripción del Trabajo**',
        'create_step2_job_placeholder': 'Pega la descripción del trabajo aquí...\n\nIncluye:\n• Requisitos\n• Responsabilidades\n• Habilidades necesarias\n• Información de la empresa',
        'create_step2_job_help': 'Pega la oferta de trabajo completa',
        'create_step2_job_url': 'O pega la URL de la oferta de trabajo',
        'create_step2_job_url_help': 'Extraeremos el contenido automáticamente',
        'create_step2_extracting': 'Extrayendo detalles del trabajo...',
        'create_step2_extracted': '✅ ¡Contenido extraído!',
        'create_step2_complete_msg': '💡 Completa tanto el currículum como la descripción del trabajo para continuar',
        'create_step3_title': '### 3️⃣ Personaliza Tu Carta',
        'create_step3_template': '📋 Elegir Plantilla',
        'create_step3_template_help': 'Selecciona una plantilla específica de la industria',
        'create_step3_preview': '👁️ Vista Previa de Plantilla',
        'create_step3_emphasis': '**🎯 Áreas de Énfasis**',
        'create_step3_emphasis_help': 'Resalta fortalezas específicas',
        'create_step3_keywords': '**🔑 Palabras Clave Adicionales (Opcional)**',
        'create_step3_keywords_placeholder': 'ej., Python, Agile, Liderazgo, AWS',
        'create_step3_keywords_help': 'Palabras clave adicionales para enfatizar',
        'create_step4_title': '### 4️⃣ Genera Tu Carta',
        'create_step4_options': '**Opciones de Generación**',
        'create_step4_num_versions': '📊 Número de Versiones (Prueba A/B)',
        'create_step4_num_versions_help': 'Genera múltiples versiones para comparación',
        'create_step4_analysis': '📈 Incluir Análisis de IA',
        'create_step4_analysis_help': 'Obtén sugerencias de escritura y puntuación de efectividad',
        'create_step4_error': '❌ ¡Por favor completa el Paso 2 primero!',
        'create_step4_generating': '✨ Generando {} versión(es)...',
        'create_step4_success': '✅ ¡{} versión(es) generada(s) exitosamente!',
        'create_step5_title': '### 5️⃣ Revisar y Exportar',
        'create_step5_ready': '✅ ¡{} versión(es) lista(s) para revisión!',
        'create_step5_compare': '**📊 Comparar Versiones (Prueba A/B)**',
        'create_step5_version': '**Versión {}**',
        'create_step5_words': '📊 {} palabras',
        'create_step5_selected': '¡Seleccionada!',
        'create_step5_your_letter': 'Tu Carta de Presentación',
        'create_step5_edit_help': 'Puedes editar la carta directamente aquí',
        'create_step5_word_count': '📊 Recuento de palabras: {} palabras',
        'create_step5_export_title': '### 📤 Opciones de Exportación',
        'create_step5_creating_pdf': 'Creando PDF...',
        'create_step5_word_coming': '¡La función de exportación a Word próximamente!',
        'create_step5_copy_msg': '✅ Usa Ctrl+C para copiar del área de texto de arriba',
        'create_step5_saved': '¡✅ Guardado en el historial!',
        'create_step5_generate_first': '💡 ¡Genera una carta primero para verla aquí!',
        
        # Emphasis Areas
        'emphasis_technical': 'Habilidades Técnicas',
        'emphasis_leadership': 'Liderazgo',
        'emphasis_problem': 'Resolución de Problemas',
        'emphasis_innovation': 'Innovación',
        'emphasis_team': 'Colaboración en Equipo',
        'emphasis_project': 'Gestión de Proyectos',
        'emphasis_customer': 'Enfoque al Cliente',
        'emphasis_results': 'Resultados y Métricas',
        
        # Tab 2: Analysis & Scoring
        'analysis_title': '## 📊 Análisis y Puntuación con IA',
        'analysis_generate_first': '💡 ¡Genera una carta de presentación primero para ver el análisis y puntuación!',
        'analysis_overall_title': '### 🎯 Puntuación General de Efectividad',
        'analysis_overall_score': 'Puntuación General',
        'analysis_ats_score': 'Puntuación ATS',
        'analysis_grammar_score': 'Gramática',
        'analysis_keywords_score': 'Palabras Clave',
        'analysis_skills_score': 'Coincidencia de Habilidades',
        'analysis_score_label': '**Puntuación: {}/100**',
        'analysis_strengths': '**✅ Fortalezas:**',
        'analysis_improvements': '**⚠️ Mejoras:**',
        'analysis_ats_title': '🎯 Análisis de Optimización ATS',
        'analysis_grammar_title': '✍️ Análisis de Gramática y Estilo',
        'analysis_issues_found': '**Problemas Encontrados:**',
        'analysis_no_issues': '✅ ¡No se detectaron problemas gramaticales!',
        'analysis_keywords_title': '🔑 Análisis de Palabras Clave',
        'analysis_coverage': '**Cobertura: {}%**',
        'analysis_matched_keywords': '**✅ Palabras Clave Coincidentes:**',
        'analysis_missing_keywords': '**⚠️ Palabras Clave Faltantes:**',
        'analysis_skills_title': '💼 Análisis de Coincidencia de Habilidades',
        'analysis_match': '**Coincidencia: {}%**',
        'analysis_highlighted_skills': '**✅ Habilidades Destacadas:**',
        'analysis_consider_adding': '**💡 Considera Agregar:**',
        'analysis_suggestions_title': '### 🤖 Sugerencias de Mejora con IA',
        'analysis_suggestion': '💡 Sugerencia {}: {}',
        'analysis_applied': '✅ ¡Sugerencia aplicada! Regenera para ver los cambios.',
        
        # Tab 3: History & Versions
        'history_title': '## 📚 Gestión de Historial y Versiones',
        'history_empty': '💡 No hay cartas guardadas aún. ¡Genera y guarda tu primera carta!',
        'history_count': '✅ Tienes {} carta(s) guardada(s)',
        'history_search': '🔍 Buscar cartas',
        'history_search_placeholder': 'Buscar por palabras clave, industria, etc.',
        'history_filter_industry': 'Filtrar por Industria',
        'history_filter_all': 'Todas',
        'history_sort': 'Ordenar por',
        'history_sort_newest': 'Más Reciente',
        'history_sort_oldest': 'Más Antigua',
        'history_sort_score': 'Puntuación',
        'history_letter_title': '📄 Carta #{} - {} - {}',
        'history_content': 'Contenido',
        'history_metadata': '**Metadatos:**',
        'history_industry': 'Industria: {}',
        'history_mode': 'Modo: {}',
        'history_template': 'Plantilla: {}',
        'history_score': 'Puntuación',
        'history_loaded': '✅ ¡Cargada como plantilla!',
        'history_deleted': '✅ ¡Eliminada!',
        'history_exporting': 'Exportando todas las cartas...',
        'history_confirm_clear': 'Estoy seguro de que quiero eliminar todas las cartas',
        'history_cleared': '✅ ¡Todo el historial borrado!',
        
        # Tab 4: Profile & Settings
        'profile_title': '## 👤 Perfil y Configuración',
        'profile_personal_info': '### Información Personal',
        'profile_name': 'Nombre Completo *',
        'profile_name_placeholder': 'Juan Pérez',
        'profile_email': 'Dirección de Email *',
        'profile_email_placeholder': 'juan.perez@email.com',
        'profile_phone': 'Número de Teléfono',
        'profile_phone_placeholder': '+34 123 456 789',
        'profile_location': 'Ubicación',
        'profile_location_placeholder': 'Madrid, España',
        'profile_linkedin': 'URL de LinkedIn',
        'profile_linkedin_placeholder': 'https://linkedin.com/in/juanperez',
        'profile_portfolio': 'Portafolio/Sitio Web',
        'profile_portfolio_placeholder': 'https://juanperez.com',
        'profile_years': 'Años de Experiencia',
        'profile_title_field': 'Puesto Actual/Reciente',
        'profile_title_placeholder': 'Ingeniero de Software Senior',
        'profile_summary': '### Resumen Profesional',
        'profile_summary_label': 'Breve resumen profesional (opcional)',
        'profile_summary_placeholder': 'Un breve resumen de tu trayectoria profesional...',
        'profile_skills': '### Habilidades Clave',
        'profile_skills_label': 'Lista tus habilidades clave (separadas por comas)',
        'profile_skills_placeholder': 'Python, JavaScript, Gestión de Proyectos, Liderazgo',
        'profile_required_error': '❌ ¡El nombre y el email son obligatorios!',
        'profile_saved': '✅ ¡Perfil guardado exitosamente!',
        'profile_settings': '### ⚙️ Configuración de la Aplicación',
        'profile_notifications': '🔔 Habilitar notificaciones',
        'profile_autosave': '💾 Guardado automático de borradores',
        'profile_analytics': '📊 Mostrar análisis avanzado',
        'profile_animations': '🎨 Habilitar animaciones',
        'profile_email_export': '📧 Enviar copias de exportación por email',
        'profile_default_length': 'Longitud predeterminada de carta (palabras)',
        
        # Tab 5: Guide & Examples
        'guide_title': '## 📖 Guía Completa y Ejemplos',
        'guide_quick_start': 'Inicio Rápido',
        'guide_best_practices': 'Mejores Prácticas',
        'guide_examples': 'Ejemplos',
        'guide_ats_tips': 'Consejos ATS',
        'guide_faq': 'Preguntas Frecuentes',
        'guide_quick_start_title': '### 🚀 Guía de Inicio Rápido',
        'guide_best_practices_title': '### ✨ Mejores Prácticas',
        'guide_examples_title': '### 📚 Ejemplos por Industria',
        'guide_ats_tips_title': '### 🎯 Consejos ATS',
        'guide_faq_title': '### ❓ Preguntas Frecuentes',
        
        # Industries
        'industry_technology': 'Tecnología',
        'industry_finance': 'Finanzas y Banca',
        'industry_healthcare': 'Salud y Medicina',
        'industry_education': 'Educación y Academia',
        'industry_marketing': 'Marketing y Publicidad',
        'industry_sales': 'Ventas y Desarrollo de Negocios',
        'industry_engineering': 'Ingeniería y Manufactura',
        'industry_legal': 'Legal y Cumplimiento',
        'industry_design': 'Diseño y Creatividad',
        'industry_hospitality': 'Hospitalidad y Servicio',
        'industry_real_estate': 'Bienes Raíces',
        'industry_consulting': 'Consultoría',
        'industry_nonprofit': 'Organizaciones sin Fines de Lucro y Servicios Sociales',
        'industry_government': 'Gobierno y Sector Público',
        
        # Template Previews
        'template_preview_title': '**Vista Previa: Plantilla {}**',
        'template_emphasizes': 'Esta plantilla enfatiza:',
        'template_tone': 'Tono:',
        'template_length': 'Longitud:',
        'template_not_available': 'Vista previa de plantilla no disponible. Esta plantilla se personalizará según tus entradas.',
        
        # Scoring & Effectiveness
        'grade_a': 'A',
        'grade_b': 'B',
        'grade_c': 'C',
        'grade_d': 'D',
        'grade_f': 'F',
        'effectiveness_exceptional': 'Excepcional - Muy probable que impresione a los reclutadores',
        'effectiveness_excellent': 'Excelente - Gran oportunidad de conseguir entrevista',
        'effectiveness_good': 'Buena - Aplicación competitiva',
        'effectiveness_fair': 'Aceptable - Necesita algunas mejoras',
        'effectiveness_needs_work': 'Necesita Trabajo - Requiere revisión significativa',
        
        # Suggestions
        'suggestion_ats_title': 'Mejorar Compatibilidad ATS',
        'suggestion_ats_desc': 'Tu carta puede no pasar la evaluación automática. Agrega más palabras clave de la descripción del trabajo y usa formato estándar.',
        'suggestion_ats_example': 'Revisa la oferta de trabajo e incorpora naturalmente términos clave como habilidades requeridas, calificaciones y tecnologías.',
        'suggestion_grammar_title': 'Corregir Problemas de Gramática y Estilo',
        'suggestion_grammar_desc': 'Hay problemas de gramática o estilo que podrían afectar tu credibilidad. Revísalos y corrígelos.',
        'suggestion_grammar_example': 'Usa nuestro corrector gramatical para identificar y corregir problemas específicos.',
        'suggestion_keywords_title': 'Agregar Más Palabras Clave Relevantes',
        'suggestion_keywords_desc': 'Tu carta carece de palabras clave importantes de la descripción del trabajo.',
        'suggestion_keywords_example': 'Revisa la sección "Palabras Clave Faltantes" e incorpóralas naturalmente en tu carta.',
        'suggestion_structure_title': 'Mejorar Estructura de la Carta',
        'suggestion_structure_desc': 'La estructura de tu carta podría ser más clara. Usa 3-4 párrafos distintos.',
        'suggestion_structure_example': 'Párrafo 1: Apertura con entusiasmo\nPárrafos 2-3: Experiencia relevante y logros\nPárrafo 4: Cierre fuerte con llamado a la acción',
        'suggestion_personal_title': 'Hacerla Más Personal y Específica',
        'suggestion_personal_desc': 'Tu carta se siente genérica. Agrega detalles específicos sobre la empresa y el puesto.',
        'suggestion_personal_example': 'Investiga la empresa y menciona: productos/proyectos específicos, valores de la empresa, noticias recientes, o por qué te entusiasma ESTE puesto en ESTA empresa.',
        'suggestion_quantify_title': 'Agregar Logros Cuantificables',
        'suggestion_quantify_desc': 'Incluye números específicos, porcentajes o métricas para demostrar impacto.',
        'suggestion_quantify_example': 'En lugar de "mejoré el rendimiento", di "mejoré el rendimiento en un 35%" o "lideré un equipo de 8 ingenieros"',
        'suggestion_active_title': 'Usar Más Voz Activa',
        'suggestion_active_desc': 'Se encontraron {} instancias de voz pasiva. La voz activa es más atractiva.',
        'suggestion_active_example': 'Cambia "El proyecto fue completado por mí" a "Completé el proyecto"',
        
        # Common Messages
        'msg_loading': 'Cargando...',
        'msg_success': '¡Éxito!',
        'msg_error': 'Error',
        'msg_warning': 'Advertencia',
        'msg_info': 'Información',
    }
}


def get_text(key: str, lang: str = 'en') -> str:
    """
    Retrieve translated text for a given key and language.
    
    Args:
        key (str): The translation key to look up
        lang (str): Language code ('en' or 'es'). Defaults to 'en'
    
    Returns:
        str: The translated text, or the key itself if translation not found
    
    Examples:
        >>> get_text('app_title', 'en')
        'CoverLetterPro'
        >>> get_text('app_title', 'es')
        'CoverLetterPro'
        >>> get_text('btn_generate', 'es')
        '🚀 Generar Carta(s) de Presentación'
    """
    # Validate language code
    if lang not in TRANSLATIONS:
        lang = 'en'  # Fallback to English
    
    # Get translation or return key if not found
    return TRANSLATIONS.get(lang, {}).get(key, key)


def get_all_translations(lang: str = 'en') -> dict:
    """
    Get all translations for a specific language.
    
    Args:
        lang (str): Language code ('en' or 'es'). Defaults to 'en'
    
    Returns:
        dict: Dictionary containing all translations for the language
    """
    if lang not in TRANSLATIONS:
        lang = 'en'
    
    return TRANSLATIONS.get(lang, {})


def get_available_languages() -> list:
    """
    Get list of available language codes.
    
    Returns:
        list: List of available language codes
    """
    return list(TRANSLATIONS.keys())


def get_language_display_names() -> dict:
    """
    Get display names for available languages.
    
    Returns:
        dict: Dictionary mapping language codes to display names
    """
    return {
        'en': 'English',
        'es': 'Español'
    }
