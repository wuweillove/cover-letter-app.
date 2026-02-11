import google.generativeai as genai
import streamlit as st
from typing import Dict, List, Optional
import time

class AIGenerator:
    """AI-powered cover letter generation using Google Gemini."""
    
    def __init__(self):
        try:
            api_key = st.secrets.get("GOOGLE_API_KEY")
            if api_key:
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
            else:
                self.model = None
        except Exception as e:
            st.error(f"⚠️ API configuration error: {str(e)}")
            self.model = None
    
    def generate_letter(self, resume: str, job_desc: str, industry: str,
                       experience: str, mode: str, template: str,
                       emphasis: List[str], variation: int = 0) -> str:
        """Generate a cover letter with AI."""
        
        if not self.model:
            return self._generate_fallback_letter(resume, job_desc)
        
        try:
            prompt = self._create_advanced_prompt(
                resume, job_desc, industry, experience, mode, template, emphasis, variation
            )
            
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7 + (variation * 0.1),  # Vary temperature for different versions
                    top_p=0.9,
                    top_k=40,
                    max_output_tokens=2048,
                )
            )
            
            if response and response.text:
                return response.text
            else:
                return self._generate_fallback_letter(resume, job_desc)
        
        except Exception as e:
            st.error(f"Generation error: {str(e)}")
            return self._generate_fallback_letter(resume, job_desc)
    
    def _create_advanced_prompt(self, resume: str, job_desc: str, industry: str,
                               experience: str, mode: str, template: str,
                               emphasis: List[str], variation: int) -> str:
        """Create an advanced, highly specific prompt."""
        
        emphasis_text = ", ".join(emphasis) if emphasis else "overall qualifications"
        
        # Variation-specific instructions
        variation_instructions = [
            "Focus on technical achievements and quantifiable results.",
            "Emphasize cultural fit and company alignment.",
            "Highlight leadership and initiative-taking."
        ]
        
        variation_instruction = variation_instructions[variation % len(variation_instructions)]
        
        prompt = f"""You are an expert cover letter writer specializing in {industry} industry applications.

TASK: Write a compelling, ATS-optimized cover letter for a {experience} candidate.

WRITING STYLE: {mode}
INDUSTRY: {industry}
EXPERIENCE LEVEL: {experience}
TEMPLATE: {template}
EMPHASIS AREAS: {emphasis_text}

VARIATION FOCUS: {variation_instruction}

CANDIDATE RESUME:
{resume[:3000]}

JOB DESCRIPTION:
{job_desc[:3000]}

REQUIREMENTS:
1. **Opening Paragraph (Hook)**:
   - Mention the specific role and company
   - Express genuine enthusiasm
   - Include a compelling reason for interest
   - Make it memorable and unique

2. **Body Paragraphs (2-3)**:
   - Paragraph 1: Highlight most relevant experience with specific examples
   - Paragraph 2: Showcase achievements with metrics (percentages, numbers, impact)
   - Paragraph 3: Demonstrate company knowledge and cultural alignment
   - Naturally incorporate keywords from job description
   - Focus strongly on: {emphasis_text}

3. **Closing Paragraph**:
   - Reiterate enthusiasm
   - Call to action for interview
   - Thank them professionally
   - Leave door open for follow-up

4. **Formatting**:
   - Use [Your Name], [Your Email], [Your Phone], [Date] as placeholders
   - Include [Hiring Manager's Name] and [Company Name] placeholders
   - Clear paragraph breaks
   - Professional business letter format

5. **ATS OPTIMIZATION**:
   - Use exact keywords from job description naturally
   - Include role title verbatim
   - Standard formatting (no tables, columns, or special characters)
   - Action verbs: achieved, developed, led, implemented, created, etc.

6. **TONE**:
   - Match the {mode} style precisely
   - Be authentic and confident
   - Show personality while staying professional
   - Avoid clichés and generic phrases

7. **LENGTH**: 300-400 words optimal

8. **MUST INCLUDE**:
   - At least 2-3 specific quantifiable achievements
   - Connection between candidate's experience and job requirements
   - Evidence of research about the company
   - Clear value proposition

Generate the cover letter now:"""
        
        return prompt
    
    def _generate_fallback_letter(self, resume: str, job_desc: str) -> str:
        """Generate a basic fallback letter if AI fails."""
        return f"""[Your Name]
[Your Email] | [Your Phone]
[Your Location]

[Date]

[Hiring Manager's Name]
[Company Name]
[Company Address]

Dear Hiring Manager,

I am writing to express my strong interest in the position at [Company Name]. With my background and experience, I am confident I would be a valuable addition to your team.

Throughout my career, I have developed strong skills and achieved measurable results. My experience aligns well with the requirements outlined in your job description, and I am particularly excited about the opportunity to contribute to [Company Name]'s mission.

I have demonstrated success in key areas including:
• Relevant technical and professional skills
• Problem-solving and analytical abilities
• Team collaboration and communication
• Project delivery and results orientation

I am impressed by [Company Name]'s work in the industry and would welcome the opportunity to discuss how my background and skills would benefit your team. Thank you for considering my application.

I look forward to speaking with you soon.

Sincerely,
[Your Name]

Note: AI generation is temporarily unavailable. Please edit this template with your specific information.
"""
    
    def improve_letter(self, current_letter: str, feedback: str) -> str:
        """Improve an existing letter based on feedback."""
        if not self.model:
            return current_letter
        
        try:
            prompt = f"""Improve this cover letter based on the following feedback:

FEEDBACK: {feedback}

CURRENT LETTER:
{current_letter}

Provide an improved version that addresses the feedback while maintaining the letter's core message and structure. Keep the same length and format.

IMPROVED LETTER:"""
            
            response = self.model.generate_content(prompt)
            
            if response and response.text:
                return response.text
            return current_letter
        
        except Exception:
            return current_letter
    
    def generate_multiple_versions(self, resume: str, job_desc: str, 
                                  count: int = 3, **kwargs) -> List[str]:
        """Generate multiple versions for A/B testing."""
        versions = []
        
        for i in range(count):
            letter = self.generate_letter(resume, job_desc, variation=i, **kwargs)
            versions.append(letter)
            time.sleep(1)  # Rate limiting
        
        return versions
