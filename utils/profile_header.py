"""Modern profile header component with dropdown menu and avatar."""
import streamlit as st

def render_profile_header(profile_manager):
    """Render modern profile header with avatar and dropdown menu."""
    profile = profile_manager.get_profile()
    completion = profile_manager.get_profile_completion_percentage()
    initials = profile_manager.get_initials()
    
    # Create header HTML
    avatar_html = f"""
    <div class="avatar-preview">
        {'<img src="' + profile.get('avatar_url', '') + '" alt="Profile">' if profile.get('avatar_url') else initials}
    </div>
    """
    
    header_html = f"""
    <div class="profile-header">
        <div class="profile-header-left">
            {avatar_html}
            <div class="profile-info">
                <h1>Hi, {profile.get('name', 'User').split()[0]}! 👋</h1>
                <p>{profile.get('current_title', 'Professional')}</p>
            </div>
        </div>
        <div class="profile-completion">
            <div class="profile-completion-label">Profile Complete</div>
            <div class="profile-completion-value">{completion}%</div>
        </div>
    </div>
    """
    
    st.markdown(header_html, unsafe_allow_html=True)
    
    # Add profile progress bar
    st.progress(completion / 100)
    
    return profile

def render_profile_section_enhanced(profile_manager):
    \"\"\"Enhanced profile section with avatar upload and modern design.\"\"\"
    profile = profile_manager.get_profile()
    initials = profile_manager.get_initials()
    
    st.markdown(\"\"\"
    <div class="section-title">
        <span class="section-icon">👤</span>
        <h3>Your Professional Profile</h3>
    </div>
    \"\"\", unsafe_allow_html=True)
    
    # Avatar Upload Section
    col_avatar, col_info = st.columns([1, 2])
    
    with col_avatar:\n        st.markdown(\"\"\"
        <div class="avatar-upload">
            <div class="avatar-preview\">
        \"\"\", unsafe_allow_html=True)
        
        if profile.get('avatar_url'):
            st.markdown(f'<img src=\"{profile[\"avatar_url\"]}\" alt=\"Avatar\">', unsafe_allow_html=True)
        else:
            st.markdown(f'<span>{initials}</span>', unsafe_allow_html=True)
        
        st.markdown(\"</div></div>\", unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            \"Upload Photo\",
            type=['png', 'jpg', 'jpeg'],
            help=\"Upload a professional profile photo\",
            key=\"avatar_upload\"
        )
        
        if uploaded_file:
            if profile_manager.save_avatar(uploaded_file):
                st.success(\"✅ Avatar updated!\")\n                st.rerun()
    
    with col_info:
        st.markdown(f\"\"\"
        <div class="modern-card">
            <h3>{profile.get('name', 'Your Name')}</h3>
            <p><strong>{profile.get('current_title', 'Your Title')}</strong></p>
            <p>📧 {profile.get('email', 'email@example.com')}</p>
            <p>📍 {profile.get('location', 'Your Location')}</p>
            <p>💼 {profile.get('years_experience', 0)} years of experience</p>
        </div>
        \"\"\", unsafe_allow_html=True)
    
    st.divider()
    
    # Profile Form
    with st.form(\"enhanced_profile_form\"):
        st.markdown(\"\"\"
        <div class="profile-edit-section">
            <div class="section-title">
                <span class="section-icon">ℹ️</span>
                <h3>Personal Information</h3>
            </div>
        </div>
        \"\"\", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input(
                \"Full Name *\",
                value=profile.get('name', ''),
                placeholder=\"Sebastian Llovera\",
                help=\"Your full name as it should appear on letters\"
            )
            
            email = st.text_input(
                \"Email Address *\",
                value=profile.get('email', ''),
                placeholder=\"sebastian@example.com\",
                help=\"Professional email address\"
            )
            
            phone = st.text_input(
                \"Phone Number\",
                value=profile.get('phone', ''),
                placeholder=\"+1 (555) 123-4567\",
                help=\"Include country code\"
            )
            
            location = st.text_input(
                \"Location\",
                value=profile.get('location', ''),
                placeholder=\"San Francisco, CA\",
                help=\"City and state/country\"
            )
        
        with col2:
            current_title = st.text_input(
                \"Current/Target Job Title *\",
                value=profile.get('current_title', ''),
                placeholder=\"Senior Software Engineer\",
                help=\"Your current or target position\"
            )
            
            company = st.text_input(
                \"Current/Recent Company\",
                value=profile.get('company', ''),
                placeholder=\"Tech Innovations Inc.\",
                help=\"Your current or most recent employer\"
            )
            
            years_experience = st.number_input(
                \"Years of Experience\",
                min_value=0,
                max_value=50,
                value=profile.get('years_experience', 0),
                help=\"Total years of professional experience\"
            )
        
        st.markdown(\"\"\"
        <div class="section-title">
            <span class="section-icon">💼</span>
            <h3>Professional Summary</h3>
        </div>
        \"\"\", unsafe_allow_html=True)
        
        professional_summary = st.text_area(
            \"Professional Summary\",
            value=profile.get('professional_summary', ''),
            height=120,
            placeholder=\"A concise summary of your professional background, key achievements, and career goals...\",
            help=\"2-3 sentences about your professional background\",
            label_visibility=\"collapsed\"
        )
        
        bio = st.text_area(
            \"Bio (Optional)\",
            value=profile.get('bio', ''),
            height=80,
            placeholder=\"A brief personal statement...\",
            help=\"Optional personal statement\"
        )
        
        key_skills = st.text_area(
            \"Key Skills (comma-separated)\",
            value=profile.get('key_skills', ''),
            height=80,
            placeholder=\"JavaScript, Python, Project Management, Leadership, AWS, React, Node.js\",
            help=\"List your top technical and soft skills\"
        )
        
        st.markdown(\"\"\"
        <div class="section-title">
            <span class="section-icon">🔗</span>
            <h3>Social & Professional Links</h3>
        </div>
        \"\"\", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            linkedin = st.text_input(
                \"LinkedIn\",
                value=profile.get('linkedin', ''),
                placeholder=\"https://linkedin.com/in/username\",
                help=\"Your LinkedIn profile URL\"
            )
        
        with col2:
            github = st.text_input(
                \"GitHub\",
                value=profile.get('github', ''),
                placeholder=\"https://github.com/username\",
                help=\"Your GitHub profile URL\"
            )
        
        with col3:
            portfolio = st.text_input(
                \"Portfolio/Website\",
                value=profile.get('portfolio', ''),
                placeholder=\"https://yourwebsite.com\",
                help=\"Personal website or portfolio\"
            )
        
        st.divider()
        
        # Submit button
        submitted = st.form_submit_button(
            \"💾 Save Profile\",
            type=\"primary\",
            use_container_width=True
        )
        
        if submitted:
            if not name or not email or not current_title:
                st.error(\"❌ Please fill in all required fields (marked with *)\")\n            else:
                profile_data = {\n                    **profile,  # Keep existing data
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'location': location,
                    'current_title': current_title,
                    'company': company,
                    'years_experience': years_experience,
                    'professional_summary': professional_summary,
                    'bio': bio,
                    'key_skills': key_skills,
                    'linkedin': linkedin,
                    'github': github,
                    'portfolio': portfolio
                }
                
                if profile_manager.save_profile(profile_data):
                    st.success(\"✅ Profile saved successfully!\")\n                    st.balloons()
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(\"❌ Error saving profile. Please try again.\")\n    \n    # Profile Stats\n    st.divider()\n    st.markdown(\"### 📊 Profile Statistics\")\n    \n    col1, col2, col3 = st.columns(3)\n    with col1:\n        st.metric(\"Profile Completion\", f\"{completion}%\")\n    with col2:\n        skills_count = len([s.strip() for s in profile.get('key_skills', '').split(',') if s.strip()])\n        st.metric(\"Skills Listed\", skills_count)\n    with col3:\n        links_count = sum(1 for link in ['linkedin', 'github', 'portfolio'] if profile.get(link))\n        st.metric(\"Social Links\", links_count)\n    \n    # Display skills\n    if profile.get('key_skills'):\n        st.markdown(\"### 🎯 Your Skills\")\n        skills = [s.strip() for s in profile['key_skills'].split(',') if s.strip()]\n        skills_html = ' '.join([f'<span class=\"skill-badge\">{skill}</span>' for skill in skills])\n        st.markdown(skills_html, unsafe_allow_html=True)
"}