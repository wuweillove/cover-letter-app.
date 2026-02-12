import streamlit as st
import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent))

from utils.theme_manager import ThemeManager, apply_custom_css
from utils.profile_manager import ProfileManager
from utils.templates import TemplateManager
from utils.ats_optimizer import ATSOptimizer
from utils.keyword_analyzer import KeywordAnalyzer
from utils.skill_matcher import SkillMatcher
from utils.grammar_checker import GrammarChecker
from utils.pdf_exporter import PDFExporter
from utils.scoring import LetterScorer
from utils.ai_generator import AIGenerator
from utils.version_manager import VersionManager
from utils.translations import get_text, get_language_display_names
import datetime
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="CoverLetterPro - Professional Cover Letter Builder",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INITIALIZE MANAGERS ---
if 'theme_manager' not in st.session_state:
    st.session_state.theme_manager = ThemeManager()
if 'profile_manager' not in st.session_state:
    st.session_state.profile_manager = ProfileManager()
if 'template_manager' not in st.session_state:
    st.session_state.template_manager = TemplateManager()
if 'version_manager' not in st.session_state:
    st.session_state.version_manager = VersionManager()
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1
if 'generated_versions' not in st.session_state:
    st.session_state.generated_versions = []
if 'show_success_modal' not in st.session_state:
    st.session_state.show_success_modal = False
# Initialize language if not set
if 'language' not in st.session_state:
    st.session_state.language = 'en'

# Apply theme
theme = st.session_state.theme_manager
apply_custom_css(theme.get_current_theme())

# --- HEADER WITH THEME TOGGLE ---
col1, col2, col3 = st.columns([6, 1, 1])
with col1:
    # Get current language for translations
    lang = st.session_state.language
    st.markdown(f"""
    <div class="main-header">
        <h1>📄 {get_text('app_title', lang)}</h1>
        <p class="subtitle">{get_text('app_subtitle', lang)}</p>
        <p class="tagline">{get_text('app_tagline', lang)}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if st.button("🌓 Theme", key="theme_toggle", help="Toggle light/dark mode"):
        theme.toggle_theme()
        st.rerun()

with col3:
    if st.button("👤 Profile", key="profile_btn", help="Manage your profile"):
        st.session_state.show_profile = True

# --- SIDEBAR ---
with st.sidebar:
    lang = st.session_state.language  # Get current language for sidebar
    st.markdown(f"### {get_text('sidebar_config', lang)}")
    
    # Profile Quick View
    profile = st.session_state.profile_manager.get_profile()
    if profile and profile.get('name'):
        st.info(get_text('sidebar_profile_set', lang).format(profile['name'], profile.get('email', '')))
    else:
        st.warning(get_text('sidebar_no_profile', lang))
    
    st.divider()
    
    # Language Selection
    lang_display_names = get_language_display_names()
    
    # Create list of language display names
    language_options = list(lang_display_names.values())
    # Find current selection index
    current_lang_name = lang_display_names.get(lang, 'English')
    default_index = language_options.index(current_lang_name) if current_lang_name in language_options else 0
    
    selected_language = st.selectbox(
        get_text('sidebar_language', lang),
        language_options,
        index=default_index,
        help=get_text('sidebar_language_help', lang)
    )
    
    # Update session state based on selection
    # Map display name back to language code
    lang_code_map = {v: k for k, v in lang_display_names.items()}
    st.session_state.language = lang_code_map.get(selected_language, 'en')
    
    # Industry Selection
    industries = st.session_state.template_manager.get_industries()
    selected_industry = st.selectbox(
        get_text('sidebar_industry', lang),
        industries,
        help=get_text('sidebar_industry_help', lang)
    )
    
    # Experience Level
    experience_level = st.selectbox(
        get_text('sidebar_experience', lang),
        [
            get_text('exp_entry', lang),
            get_text('exp_mid', lang),
            get_text('exp_senior', lang),
            get_text('exp_executive', lang)
        ],
        help=get_text('sidebar_experience_help', lang)
    )
    
    # Writing Mode
    writing_mode = st.selectbox(
        get_text('sidebar_writing_mode', lang),
        [
            get_text('mode_professional', lang),
            get_text('mode_confident', lang),
            get_text('mode_creative', lang),
            get_text('mode_technical', lang),
            get_text('mode_friendly', lang)
        ],
        help=get_text('sidebar_writing_mode_help', lang)
    )
    
    # Letter Length
    letter_length = st.select_slider(
        get_text('sidebar_letter_length', lang),
        options=[
            get_text('length_concise', lang),
            get_text('length_standard', lang),
            get_text('length_detailed', lang)
        ],
        value=get_text('length_standard', lang),
        help=get_text('sidebar_letter_length_help', lang)
    )
    
    st.divider()
    
    # Statistics
    st.markdown(f"### {get_text('sidebar_statistics', lang)}")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(get_text('sidebar_letters', lang), len(st.session_state.version_manager.get_all_versions()))
    with col2:
        st.metric(get_text('sidebar_versions', lang), len(st.session_state.generated_versions))
    
    st.divider()
    
    # Quick Tips
    with st.expander(get_text('sidebar_pro_tips', lang)):
        st.markdown(f"""
        {get_text('tips_title', lang)}
        {get_text('tips_1', lang)}
        {get_text('tips_2', lang)}
        {get_text('tips_3', lang)}
        {get_text('tips_4', lang)}
        {get_text('tips_5', lang)}
        """)
    
    # Success Stories
    with st.expander(get_text('sidebar_success_stories', lang)):
        st.markdown(f"""
        {get_text('story_1_quote', lang)}
        {get_text('story_1_author', lang)}
        
        {get_text('story_2_quote', lang)}
        {get_text('story_2_author', lang)}
        
        {get_text('story_3_quote', lang)}
        {get_text('story_3_author', lang)}
        """)

# --- PROGRESS INDICATOR ---
lang = st.session_state.language  # Get current language
st.markdown(f"### {get_text('progress_title', lang)}")
progress_steps = [
    get_text('step_profile', lang),
    get_text('step_input', lang),
    get_text('step_customize', lang),
    get_text('step_generate', lang),
    get_text('step_review', lang)
]
current_step = st.session_state.current_step

progress_html = '<div class="progress-container">'
for i, step in enumerate(progress_steps, 1):
    status = "completed" if i < current_step else ("active" if i == current_step else "pending")
    icon = "✅" if i < current_step else ("🔵" if i == current_step else "⚪")
    progress_html += f'<div class="progress-step {status}">{icon} {step}</div>'
progress_html += '</div>'

st.markdown(progress_html, unsafe_allow_html=True)
st.progress(current_step / len(progress_steps))

st.divider()

# --- MAIN TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    get_text('tab_create', lang),
    get_text('tab_analysis', lang),
    get_text('tab_history', lang),
    get_text('tab_profile', lang),
    get_text('tab_guide', lang)
])

# ============================================
# TAB 1: CREATE LETTER
# ============================================
with tab1:
    st.markdown("## Step-by-Step Letter Creation")
    
    # STEP 1: Profile Check
    with st.expander("### 1️⃣ Profile Information", expanded=current_step==1):
        if not profile or not profile.get('name'):
            st.warning("⚠️ Please complete your profile in the 'Profile & Settings' tab first!")
            if st.button("Go to Profile", key="goto_profile"):
                st.session_state.current_step = 4
                st.rerun()
        else:
            st.success(f"✅ Profile ready: {profile['name']}")
            if st.button("Continue to Input →", key="step1_continue"):
                st.session_state.current_step = 2
                st.rerun()
    
    # STEP 2: Input Data
    with st.expander("### 2️⃣ Input Your Information", expanded=current_step==2):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📄 Your Resume/Experience**")
            resume_input = st.text_area(
                "Resume Content",
                height=300,
                placeholder="Paste your resume here...\n\nInclude:\n• Work experience\n• Skills\n• Achievements\n• Education",
                help="Upload or paste your complete resume",
                label_visibility="collapsed"
            )
            
            # File upload
            uploaded_resume = st.file_uploader(
                "Or upload resume (PDF/DOCX)",
                type=['pdf', 'docx', 'txt'],
                key="resume_upload"
            )
            
            if uploaded_resume:
                st.info(f"📄 File: {uploaded_resume.name}")
            
            st.caption(f"📊 Characters: {len(resume_input)}")
        
        with col2:
            st.markdown("**💼 Job Description**")
            job_input = st.text_area(
                "Job Description",
                height=300,
                placeholder="Paste job description here...\n\nInclude:\n• Requirements\n• Responsibilities\n• Skills needed\n• Company info",
                help="Paste the complete job posting",
                label_visibility="collapsed"
            )
            
            # URL input
            job_url = st.text_input(
                "Or paste job posting URL",
                placeholder="https://...",
                help="We'll extract the content automatically"
            )
            
            if job_url and st.button("🔗 Extract from URL", key="extract_url"):
                with st.spinner("Extracting job details..."):
                    # URL extraction logic would go here
                    st.success("✅ Content extracted!")
            
            st.caption(f"📊 Characters: {len(job_input)}")
        
        # Continue button
        if resume_input and job_input:
            if st.button("Continue to Customization →", key="step2_continue", type="primary"):
                st.session_state.resume_data = resume_input
                st.session_state.job_data = job_input
                st.session_state.current_step = 3
                st.rerun()
        else:
            st.info("💡 Complete both resume and job description to continue")
    
    # STEP 3: Customize
    with st.expander("### 3️⃣ Customize Your Letter", expanded=current_step==3):
        # Template selection
        templates = st.session_state.template_manager.get_templates_by_industry(selected_industry)
        selected_template = st.selectbox(
            "📋 Choose Template",
            templates,
            help="Select an industry-specific template"
        )
        
        # Preview template
        if selected_template:
            template_preview = st.session_state.template_manager.get_template_preview(selected_template)
            with st.expander("👁️ Preview Template"):
                st.markdown(template_preview)
        
        # Emphasis areas
        st.markdown("**🎯 Emphasis Areas**")
        emphasis_areas = st.multiselect(
            "Select focus areas",
            ["Technical Skills", "Leadership", "Problem Solving", "Innovation", 
             "Team Collaboration", "Project Management", "Customer Focus", "Results & Metrics"],
            default=["Technical Skills"],
            help="Highlight specific strengths",
            label_visibility="collapsed"
        )
        
        # Keywords to emphasize
        st.markdown("**🔑 Additional Keywords (Optional)**")
        custom_keywords = st.text_input(
            "Comma-separated keywords",
            placeholder="e.g., Python, Agile, Leadership, AWS",
            help="Extra keywords to emphasize",
            label_visibility="collapsed"
        )
        
        if st.button("Continue to Generation →", key="step3_continue", type="primary"):
            st.session_state.template = selected_template
            st.session_state.emphasis = emphasis_areas
            st.session_state.keywords = custom_keywords
            st.session_state.current_step = 4
            st.rerun()
    
    # STEP 4: Generate
    with st.expander("### 4️⃣ Generate Your Letter", expanded=current_step==4):
        st.markdown("**Generation Options**")
        
        col1, col2 = st.columns(2)
        with col1:
            num_versions = st.slider(
                "📊 Number of Versions (A/B Testing)",
                min_value=1,
                max_value=5,
                value=2,
                help="Generate multiple versions for comparison"
            )
        
        with col2:
            include_analysis = st.checkbox(
                "📈 Include AI Analysis",
                value=True,
                help="Get writing suggestions and effectiveness score"
            )
        
        # Generate button
        if st.button("🚀 Generate Cover Letter(s)", key="generate_main", type="primary", use_container_width=True):
            if not hasattr(st.session_state, 'resume_data'):
                st.error("❌ Please complete Step 2 first!")
            else:
                with st.spinner(f"✨ Generating {num_versions} version(s)..."):
                    progress_bar = st.progress(0)
                    
                    ai_generator = AIGenerator()
                    generated_versions = []
                    
                    for i in range(num_versions):
                        progress_bar.progress((i + 1) / num_versions)
                        
                        # Generate letter
                        letter = ai_generator.generate_letter(
                            resume=st.session_state.resume_data,
                            job_desc=st.session_state.job_data,
                            industry=selected_industry,
                            experience=experience_level,
                            mode=writing_mode,
                            template=st.session_state.get('template', 'Standard'),
                            emphasis=st.session_state.get('emphasis', []),
                            variation=i
                        )
                        
                        generated_versions.append({
                            'content': letter,
                            'version': i + 1,
                            'timestamp': datetime.datetime.now(),
                            'settings': {
                                'industry': selected_industry,
                                'mode': writing_mode,
                                'template': st.session_state.get('template', 'Standard')
                            }
                        })
                        
                        time.sleep(0.5)  # Rate limiting
                    
                    st.session_state.generated_versions = generated_versions
                    st.session_state.current_step = 5
                    st.success(f"✅ Generated {num_versions} version(s) successfully!")
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
    
    # STEP 5: Review & Export
    with st.expander("### 5️⃣ Review & Export", expanded=current_step==5):
        if st.session_state.generated_versions:
            st.success(f"✅ {len(st.session_state.generated_versions)} version(s) ready for review!")
            
            # Version selector
            if len(st.session_state.generated_versions) > 1:
                st.markdown("**📊 Compare Versions (A/B Testing)**")
                cols = st.columns(len(st.session_state.generated_versions))
                
                for idx, (col, version) in enumerate(zip(cols, st.session_state.generated_versions)):
                    with col:
                        st.markdown(f"**Version {version['version']}**")
                        st.text_area(
                            f"Version {version['version']}",
                            value=version['content'],
                            height=300,
                            key=f"version_{idx}",
                            label_visibility="collapsed"
                        )
                        
                        # Quick stats
                        word_count = len(version['content'].split())
                        st.caption(f"📊 {word_count} words")
                        
                        # Select button
                        if st.button(f"✅ Select This Version", key=f"select_v{idx}"):
                            st.session_state.selected_version = idx
                            st.success("Selected!")
            else:
                selected_version = st.session_state.generated_versions[0]
                edited_letter = st.text_area(
                    "Your Cover Letter",
                    value=selected_version['content'],
                    height=400,
                    help="You can edit the letter directly here"
                )
                st.session_state.final_letter = edited_letter
                
                word_count = len(edited_letter.split())
                st.info(f"📊 Word count: {word_count} words")
            
            st.divider()
            
            # Export options
            st.markdown("### 📤 Export Options")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                if st.button("📄 Download PDF", use_container_width=True, type="primary"):
                    with st.spinner("Creating PDF..."):
                        pdf_exporter = PDFExporter()
                        pdf_data = pdf_exporter.create_pdf(
                            content=st.session_state.get('final_letter', st.session_state.generated_versions[0]['content']),
                            profile=profile,
                            branding=True
                        )
                        st.download_button(
                            "⬇️ Download PDF",
                            pdf_data,
                            file_name="cover_letter.pdf",
                            mime="application/pdf"
                        )
            
            with col2:
                if st.button("📝 Download Word", use_container_width=True):
                    st.info("Word export feature coming soon!")
            
            with col3:
                if st.button("📋 Copy to Clipboard", use_container_width=True):
                    st.success("✅ Use Ctrl+C to copy from the text area above")
            
            with col4:
                if st.button("💾 Save to History", use_container_width=True):
                    version_mgr = st.session_state.version_manager
                    version_mgr.save_version(
                        content=st.session_state.get('final_letter', st.session_state.generated_versions[0]['content']),
                        metadata={
                            'industry': selected_industry,
                            'mode': writing_mode,
                            'template': st.session_state.get('template', 'Standard')
                        }
                    )
                    st.success("✅ Saved to history!")
        else:
            st.info("💡 Generate a letter first to see it here!")

# ============================================
# TAB 2: ANALYSIS & SCORING
# ============================================
with tab2:
    st.markdown("## 📊 AI-Powered Analysis & Scoring")
    
    if not st.session_state.generated_versions:
        st.info("💡 Generate a cover letter first to see analysis and scoring!")
    else:
        selected_version = st.session_state.generated_versions[st.session_state.get('selected_version', 0)]
        
        # Initialize analyzers
        ats_optimizer = ATSOptimizer()
        keyword_analyzer = KeywordAnalyzer()
        skill_matcher = SkillMatcher()
        grammar_checker = GrammarChecker()
        letter_scorer = LetterScorer()
        
        # Get analysis data
        if hasattr(st.session_state, 'job_data'):
            # ATS Score
            ats_score = ats_optimizer.calculate_ats_score(
                letter=selected_version['content'],
                job_description=st.session_state.job_data
            )
            
            # Keyword Analysis
            keyword_analysis = keyword_analyzer.analyze(
                letter=selected_version['content'],
                job_description=st.session_state.job_data
            )
            
            # Skills Matching
            if hasattr(st.session_state, 'resume_data'):
                skills_match = skill_matcher.match_skills(
                    resume=st.session_state.resume_data,
                    job_description=st.session_state.job_data,
                    letter=selected_version['content']
                )
            else:
                skills_match = None
            
            # Grammar Check
            grammar_results = grammar_checker.check(selected_version['content'])
            
            # Overall Score
            overall_score = letter_scorer.calculate_score(
                letter=selected_version['content'],
                ats_score=ats_score['score'],
                grammar_score=grammar_results['score'],
                keyword_score=keyword_analysis['coverage']
            )
            
            # Display Scores
            st.markdown("### 🎯 Overall Effectiveness Score")
            score_cols = st.columns(5)
            
            with score_cols[0]:
                score_color = "green" if overall_score['total'] >= 80 else ("orange" if overall_score['total'] >= 60 else "red")
                st.markdown(f"""
                <div class="score-card">
                    <div class="score-value" style="color: {score_color};">{overall_score['total']}</div>
                    <div class="score-label">Overall Score</div>
                </div>
                """, unsafe_allow_html=True)
            
            with score_cols[1]:
                st.markdown(f"""
                <div class="score-card">
                    <div class="score-value">{ats_score['score']}</div>
                    <div class="score-label">ATS Score</div>
                </div>
                """, unsafe_allow_html=True)
            
            with score_cols[2]:
                st.markdown(f"""
                <div class="score-card">
                    <div class="score-value">{grammar_results['score']}</div>
                    <div class="score-label">Grammar</div>
                </div>
                """, unsafe_allow_html=True)
            
            with score_cols[3]:
                st.markdown(f"""
                <div class="score-card">
                    <div class="score-value">{keyword_analysis['coverage']}</div>
                    <div class="score-label">Keywords</div>
                </div>
                """, unsafe_allow_html=True)
            
            with score_cols[4]:
                if skills_match:
                    st.markdown(f"""
                    <div class="score-card">
                        <div class="score-value">{skills_match['match_percentage']}</div>
                        <div class="score-label">Skills Match</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.divider()
            
            # Detailed Analysis
            col1, col2 = st.columns(2)
            
            with col1:
                # ATS Analysis
                with st.expander("🎯 ATS Optimization Analysis", expanded=True):
                    st.markdown(f"**Score: {ats_score['score']}/100**")
                    st.progress(ats_score['score'] / 100)
                    
                    st.markdown("**✅ Strengths:**")
                    for strength in ats_score.get('strengths', []):
                        st.success(f"• {strength}")
                    
                    st.markdown("**⚠️ Improvements:**")
                    for improvement in ats_score.get('improvements', []):
                        st.warning(f"• {improvement}")
                
                # Grammar Check
                with st.expander("✍️ Grammar & Style Analysis"):
                    st.markdown(f"**Score: {grammar_results['score']}/100**")
                    st.progress(grammar_results['score'] / 100)
                    
                    if grammar_results.get('issues'):
                        st.markdown("**Issues Found:**")
                        for issue in grammar_results['issues']:
                            st.warning(f"• {issue}")
                    else:
                        st.success("✅ No grammar issues detected!")
            
            with col2:
                # Keyword Analysis
                with st.expander("🔑 Keyword Analysis", expanded=True):
                    st.markdown(f"**Coverage: {keyword_analysis['coverage']}%**")
                    st.progress(keyword_analysis['coverage'] / 100)
                    
                    st.markdown("**✅ Matched Keywords:**")
                    for keyword in keyword_analysis.get('matched', []):
                        st.markdown(f"<span class='keyword-badge matched'>{keyword}</span>", unsafe_allow_html=True)
                    
                    st.markdown("**⚠️ Missing Keywords:**")
                    for keyword in keyword_analysis.get('missing', []):
                        st.markdown(f"<span class='keyword-badge missing'>{keyword}</span>", unsafe_allow_html=True)
                
                # Skills Matching
                if skills_match:
                    with st.expander("💼 Skills Matching Analysis"):
                        st.markdown(f"**Match: {skills_match['match_percentage']}%**")
                        st.progress(skills_match['match_percentage'] / 100)
                        
                        st.markdown("**✅ Highlighted Skills:**")
                        for skill in skills_match.get('matched_skills', []):
                            st.success(f"• {skill}")
                        
                        st.markdown("**💡 Consider Adding:**")
                        for skill in skills_match.get('missing_skills', []):
                            st.info(f"• {skill}")
            
            st.divider()
            
            # AI Suggestions
            st.markdown("### 🤖 AI-Powered Improvement Suggestions")
            suggestions = letter_scorer.get_suggestions(selected_version['content'], overall_score)
            
            for i, suggestion in enumerate(suggestions, 1):
                with st.expander(f"💡 Suggestion {i}: {suggestion['title']}"):
                    st.markdown(suggestion['description'])
                    if 'example' in suggestion:
                        st.code(suggestion['example'])
                    if st.button(f"Apply Suggestion {i}", key=f"apply_sug_{i}"):
                        st.success("✅ Suggestion applied! Regenerate to see changes.")

# ============================================
# TAB 3: HISTORY & VERSIONS
# ============================================
with tab3:
    st.markdown("## 📚 History & Version Management")
    
    version_mgr = st.session_state.version_manager
    all_versions = version_mgr.get_all_versions()
    
    if not all_versions:
        st.info("💡 No saved letters yet. Generate and save your first letter!")
    else:
        st.success(f"✅ You have {len(all_versions)} saved letter(s)")
        
        # Search and filter
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            search_query = st.text_input(
                "🔍 Search letters",
                placeholder="Search by keywords, industry, etc."
            )
        with col2:
            filter_industry = st.selectbox(
                "Filter by Industry",
                ["All"] + st.session_state.template_manager.get_industries()
            )
        with col3:
            sort_by = st.selectbox(
                "Sort by",
                ["Newest", "Oldest", "Score"]
            )
        
        st.divider()
        
        # Display versions
        for idx, version in enumerate(all_versions):
            with st.expander(
                f"📄 Letter #{idx + 1} - {version.get('timestamp', 'N/A')} - {version.get('metadata', {}).get('industry', 'General')}",
                expanded=False
            ):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.text_area(
                        "Content",
                        value=version['content'],
                        height=200,
                        key=f"history_{idx}",
                        label_visibility="collapsed"
                    )
                
                with col2:
                    st.markdown("**Metadata:**")
                    metadata = version.get('metadata', {})
                    st.caption(f"Industry: {metadata.get('industry', 'N/A')}")
                    st.caption(f"Mode: {metadata.get('mode', 'N/A')}")
                    st.caption(f"Template: {metadata.get('template', 'N/A')}")
                    
                    if 'score' in version:
                        st.metric("Score", version['score'])
                    
                    st.divider()
                    
                    if st.button("🔄 Use as Template", key=f"use_template_{idx}"):
                        st.session_state.template_content = version['content']
                        st.success("✅ Loaded as template!")
                    
                    if st.button("📥 Download", key=f"download_{idx}"):
                        st.download_button(
                            "⬇️ Download",
                            version['content'],
                            file_name=f"cover_letter_{idx+1}.txt",
                            mime="text/plain",
                            key=f"dl_btn_{idx}"
                        )
                    
                    if st.button("🗑️ Delete", key=f"delete_{idx}"):
                        version_mgr.delete_version(idx)
                        st.success("✅ Deleted!")
                        st.rerun()
        
        st.divider()
        
        # Bulk actions
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📥 Export All as ZIP"):
                st.info("Exporting all letters...")
        with col2:
            if st.button("🗑️ Clear All History"):
                if st.checkbox("I'm sure I want to delete all letters"):
                    version_mgr.clear_all()
                    st.success("✅ All history cleared!")
                    st.rerun()

# ============================================
# TAB 4: PROFILE & SETTINGS
# ============================================
with tab4:
    st.markdown("## 👤 Profile & Settings")
    
    profile_mgr = st.session_state.profile_manager
    current_profile = profile_mgr.get_profile()
    
    with st.form("profile_form"):
        st.markdown("### Personal Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input(
                "Full Name *",
                value=current_profile.get('name', ''),
                placeholder="John Doe"
            )
            
            email = st.text_input(
                "Email Address *",
                value=current_profile.get('email', ''),
                placeholder="john.doe@email.com"
            )
            
            phone = st.text_input(
                "Phone Number",
                value=current_profile.get('phone', ''),
                placeholder="+1 (555) 123-4567"
            )
            
            location = st.text_input(
                "Location",
                value=current_profile.get('location', ''),
                placeholder="San Francisco, CA"
            )
        
        with col2:
            linkedin = st.text_input(
                "LinkedIn URL",
                value=current_profile.get('linkedin', ''),
                placeholder="https://linkedin.com/in/johndoe"
            )
            
            portfolio = st.text_input(
                "Portfolio/Website",
                value=current_profile.get('portfolio', ''),
                placeholder="https://johndoe.com"
            )
            
            years_experience = st.number_input(
                "Years of Experience",
                min_value=0,
                max_value=50,
                value=current_profile.get('years_experience', 0)
            )
            
            current_title = st.text_input(
                "Current/Recent Job Title",
                value=current_profile.get('current_title', ''),
                placeholder="Senior Software Engineer"
            )
        
        st.markdown("### Professional Summary")
        professional_summary = st.text_area(
            "Brief professional summary (optional)",
            value=current_profile.get('professional_summary', ''),
            height=100,
            placeholder="A brief summary of your professional background...",
            label_visibility="collapsed"
        )
        
        st.markdown("### Key Skills")
        key_skills = st.text_area(
            "List your key skills (comma-separated)",
            value=current_profile.get('key_skills', ''),
            placeholder="Python, JavaScript, Project Management, Leadership",
            label_visibility="collapsed"
        )
        
        submitted = st.form_submit_button("💾 Save Profile", type="primary", use_container_width=True)
        
        if submitted:
            if not name or not email:
                st.error("❌ Name and email are required!")
            else:
                profile_data = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'location': location,
                    'linkedin': linkedin,
                    'portfolio': portfolio,
                    'years_experience': years_experience,
                    'current_title': current_title,
                    'professional_summary': professional_summary,
                    'key_skills': key_skills
                }
                
                profile_mgr.save_profile(profile_data)
                st.success("✅ Profile saved successfully!")
                st.balloons()
    
    st.divider()
    
    # Application Settings
    st.markdown("### ⚙️ Application Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("🔔 Enable notifications", value=True)
        st.checkbox("💾 Auto-save drafts", value=True)
        st.checkbox("📊 Show advanced analytics", value=False)
    
    with col2:
        st.checkbox("🎨 Enable animations", value=True)
        st.checkbox("📧 Email export copies", value=False)
        st.number_input("Default letter length (words)", min_value=200, max_value=500, value=350)

# ============================================
# TAB 5: GUIDE & EXAMPLES
# ============================================
with tab5:
    st.markdown("## 📖 Complete Guide & Examples")
    
    guide_tabs = st.tabs(["Quick Start", "Best Practices", "Examples", "ATS Tips", "FAQ"])
    
    with guide_tabs[0]:
        st.markdown("""
        ### 🚀 Quick Start Guide
        
        Complete guide content here...
        """)
    
    with guide_tabs[1]:
        st.markdown("### ✨ Best Practices")
    
    with guide_tabs[2]:
        st.markdown("### 📚 Examples by Industry")
    
    with guide_tabs[3]:
        st.markdown("### 🎯 ATS Tips")
    
    with guide_tabs[4]:
        st.markdown("### ❓ FAQ")
