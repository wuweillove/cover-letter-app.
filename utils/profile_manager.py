import streamlit as st
import json
from datetime import datetime
import base64
from io import BytesIO
from PIL import Image

class ProfileManager:
    """Enhanced Profile Manager with avatar support and advanced features."""
    
    def __init__(self):
        if 'user_profile' not in st.session_state:
            st.session_state.user_profile = self._load_profile()
    
    def _load_profile(self):
        """Load profile from session state or create default with demo data."""
        return {
            'name': 'Sebastian Llovera',
            'email': 'sebastian.llovera@example.com',
            'phone': '+1 (555) 123-4567',
            'location': 'San Francisco, CA',
            'linkedin': 'https://linkedin.com/in/sebastian-llovera',
            'portfolio': 'https://sllovera.dev',
            'github': 'https://github.com/wuweillove',
            'years_experience': 5,
            'current_title': 'Senior Full Stack Developer',
            'company': 'Tech Innovations Inc.',
            'professional_summary': 'Passionate Full Stack Developer with 5 years of experience building scalable web applications. Specialized in React, Node.js, and cloud architecture. Committed to writing clean code and delivering exceptional user experiences.',
            'key_skills': 'JavaScript, TypeScript, React, Node.js, Python, AWS, Docker, Kubernetes, PostgreSQL, MongoDB, CI/CD, Agile, Team Leadership',
            'avatar_url': '',
            'bio': 'I love solving complex problems with elegant solutions. When I\'m not coding, you can find me contributing to open source projects or mentoring junior developers.',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
    
    def get_profile(self):
        """Get current user profile."""
        return st.session_state.user_profile
    
    def save_profile(self, profile_data):
        """Save user profile data."""
        profile_data['updated_at'] = datetime.now().isoformat()
        st.session_state.user_profile = profile_data
        return True
    
    def update_profile(self, field, value):
        """Update a single profile field."""
        st.session_state.user_profile[field] = value
        st.session_state.user_profile['updated_at'] = datetime.now().isoformat()
        return True
    
    def save_avatar(self, uploaded_file):
        """Save avatar image as base64."""
        try:
            img = Image.open(uploaded_file)
            img.thumbnail((200, 200))
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            self.update_profile('avatar_url', f"data:image/png;base64,{img_str}")
            return True
        except Exception as e:
            st.error(f"Error saving avatar: {e}")
            return False
    
    def get_initials(self):
        """Get user initials from name."""
        profile = self.get_profile()
        name = profile.get('name', '')
        if name:
            parts = name.split()
            if len(parts) >= 2:
                return f"{parts[0][0]}{parts[1][0]}".upper()
            return name[0:2].upper()
        return 'SL'
    
    def clear_profile(self):
        """Clear all profile data."""
        st.session_state.user_profile = self._load_profile()
        return True
    
    def is_profile_complete(self):
        """Check if profile has minimum required fields."""
        profile = self.get_profile()
        required_fields = ['name', 'email']
        return all(profile.get(field) for field in required_fields)
    
    def get_profile_completion_percentage(self):
        """Calculate profile completion percentage."""
        profile = self.get_profile()
        fields_to_check = [
            'name', 'email', 'phone', 'location', 'linkedin', 'portfolio',
            'github', 'current_title', 'company', 'professional_summary',
            'key_skills', 'avatar_url', 'bio'
        ]
        completed_fields = sum(1 for field in fields_to_check if profile.get(field))
        return int((completed_fields / len(fields_to_check)) * 100)
    
    def export_profile(self):
        """Export profile as JSON."""
        return json.dumps(self.get_profile(), indent=2)
    
    def import_profile(self, profile_json):
        """Import profile from JSON."""
        try:
            profile_data = json.loads(profile_json)
            self.save_profile(profile_data)
            return True
        except:
            return False
