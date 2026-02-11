import streamlit as st
import json
from datetime import datetime

class ProfileManager:
    """Manages user profile data with session and local storage."""
    
    def __init__(self):
        if 'user_profile' not in st.session_state:
            st.session_state.user_profile = self._load_profile()
    
    def _load_profile(self):
        """Load profile from session state or create default."""
        # In production, this could load from a database or file
        return {
            'name': '',
            'email': '',
            'phone': '',
            'location': '',
            'linkedin': '',
            'portfolio': '',
            'years_experience': 0,
            'current_title': '',
            'professional_summary': '',
            'key_skills': '',
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
        # In production, persist to database or file
        return True
    
    def update_profile(self, field, value):
        """Update a single profile field."""
        st.session_state.user_profile[field] = value
        st.session_state.user_profile['updated_at'] = datetime.now().isoformat()
        return True
    
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
        total_fields = 10
        completed_fields = sum(1 for key in profile if profile[key] and key not in ['created_at', 'updated_at'])
        return int((completed_fields / total_fields) * 100)
    
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
