from io import BytesIO
from datetime import datetime
from typing import Dict, Optional

class PDFExporter:
    """Export cover letters to professional PDF format."""
    
    def __init__(self):
        self.default_font = 'Helvetica'
        self.default_font_size = 11
    
    def create_pdf(self, content: str, profile: Dict, branding: bool = True) -> BytesIO:
        """Create a professional PDF from cover letter content."""
        # Note: In production, use reportlab or similar library
        # This is a simplified implementation
        
        buffer = BytesIO()
        
        # Format the content
        formatted_content = self._format_letter(content, profile, branding)
        
        # For now, return as text (in production, convert to actual PDF)
        buffer.write(formatted_content.encode('utf-8'))
        buffer.seek(0)
        
        return buffer
    
    def _format_letter(self, content: str, profile: Dict, branding: bool) -> str:
        """Format letter with professional styling."""
        formatted = ""
        
        # Add header with contact info
        if profile:
            formatted += f"{profile.get('name', '')}\n"
            if profile.get('email'):
                formatted += f"Email: {profile['email']} | "
            if profile.get('phone'):
                formatted += f"Phone: {profile['phone']}\n"
            if profile.get('location'):
                formatted += f"{profile['location']}\n"
            if profile.get('linkedin'):
                formatted += f"LinkedIn: {profile['linkedin']}\n"
            formatted += "\n"
        
        # Add date
        formatted += f"{datetime.now().strftime('%B %d, %Y')}\n\n"
        
        # Add main content
        formatted += content
        
        # Add footer if branding enabled
        if branding:
            formatted += "\n\n---\n"
            formatted += "Generated with CoverLetterPro\n"
        
        return formatted
    
    def create_word_doc(self, content: str, profile: Dict) -> BytesIO:
        """Create a Word document (DOCX) from cover letter content."""
        # Note: In production, use python-docx library
        buffer = BytesIO()
        
        formatted_content = self._format_letter(content, profile, False)
        buffer.write(formatted_content.encode('utf-8'))
        buffer.seek(0)
        
        return buffer
    
    def create_plain_text(self, content: str, profile: Dict) -> str:
        """Create plain text version."""
        return self._format_letter(content, profile, False)
    
    def add_company_branding(self, content: str, company_name: str, 
                           logo_path: Optional[str] = None) -> BytesIO:
        """Add company branding to the PDF."""
        buffer = BytesIO()
        
        branded_content = f"Application to {company_name}\n\n{content}"
        buffer.write(branded_content.encode('utf-8'))
        buffer.seek(0)
        
        return buffer
