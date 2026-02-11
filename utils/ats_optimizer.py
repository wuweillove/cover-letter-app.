import re
from typing import Dict, List

class ATSOptimizer:
    """Optimizes cover letters for ATS (Applicant Tracking Systems)."""
    
    def __init__(self):
        self.ats_friendly_sections = [
            'contact information',
            'opening',
            'experience',
            'skills',
            'education',
            'closing'
        ]
    
    def calculate_ats_score(self, letter: str, job_description: str) -> Dict:
        """Calculate ATS compatibility score."""
        scores = {
            'keyword_match': self._check_keyword_match(letter, job_description),
            'formatting': self._check_formatting(letter),
            'length': self._check_length(letter),
            'action_verbs': self._check_action_verbs(letter),
            'readability': self._check_readability(letter)
        }
        
        # Calculate weighted average
        weights = {
            'keyword_match': 0.40,
            'formatting': 0.20,
            'length': 0.15,
            'action_verbs': 0.15,
            'readability': 0.10
        }
        
        total_score = sum(scores[key] * weights[key] for key in scores)
        
        return {
            'score': int(total_score),
            'breakdown': scores,
            'strengths': self._identify_strengths(scores),
            'improvements': self._identify_improvements(scores)
        }
    
    def _check_keyword_match(self, letter: str, job_description: str) -> int:
        """Check how many job description keywords are in the letter."""
        # Extract keywords from job description
        job_words = set(re.findall(r'\b[a-zA-Z]{4,}\b', job_description.lower()))
        letter_words = set(re.findall(r'\b[a-zA-Z]{4,}\b', letter.lower()))
        
        # Remove common words
        stop_words = {'that', 'this', 'with', 'from', 'have', 'will', 'your', 
                      'their', 'about', 'which', 'where', 'when', 'what', 'these',
                      'those', 'them', 'they', 'than', 'then', 'there', 'here'}
        
        job_keywords = job_words - stop_words
        matched_keywords = letter_words & job_keywords
        
        if len(job_keywords) > 0:
            match_rate = len(matched_keywords) / len(job_keywords)
            return int(match_rate * 100)
        return 50
    
    def _check_formatting(self, letter: str) -> int:
        """Check if formatting is ATS-friendly."""
        score = 100
        
        # Check for complex formatting issues
        if '\t' in letter:  # Tabs
            score -= 10
        if len(re.findall(r'[^\x00-\x7F]', letter)) > 5:  # Too many special chars
            score -= 15
        if letter.count('\n\n') < 2:  # Not enough paragraph breaks
            score -= 10
        
        return max(score, 0)
    
    def _check_length(self, letter: str) -> int:
        """Check if letter length is appropriate."""
        word_count = len(letter.split())
        
        if 250 <= word_count <= 400:
            return 100
        elif 200 <= word_count < 250 or 400 < word_count <= 450:
            return 85
        elif 150 <= word_count < 200 or 450 < word_count <= 500:
            return 70
        else:
            return 50
    
    def _check_action_verbs(self, letter: str) -> int:
        """Check usage of strong action verbs."""
        action_verbs = [
            'achieved', 'improved', 'developed', 'implemented', 'created',
            'managed', 'led', 'designed', 'optimized', 'increased',
            'reduced', 'launched', 'delivered', 'coordinated', 'executed',
            'established', 'generated', 'enhanced', 'streamlined', 'transformed'
        ]
        
        letter_lower = letter.lower()
        verb_count = sum(1 for verb in action_verbs if verb in letter_lower)
        
        if verb_count >= 5:
            return 100
        elif verb_count >= 3:
            return 80
        elif verb_count >= 1:
            return 60
        else:
            return 40
    
    def _check_readability(self, letter: str) -> int:
        """Check readability and sentence structure."""
        sentences = re.split(r'[.!?]\s+', letter)
        
        if not sentences:
            return 50
        
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)
        
        # Ideal: 15-20 words per sentence
        if 15 <= avg_sentence_length <= 20:
            return 100
        elif 12 <= avg_sentence_length < 15 or 20 < avg_sentence_length <= 25:
            return 85
        else:
            return 70
    
    def _identify_strengths(self, scores: Dict) -> List[str]:
        """Identify what's working well."""
        strengths = []
        
        if scores['keyword_match'] >= 70:
            strengths.append("Strong keyword match with job description")
        if scores['formatting'] >= 90:
            strengths.append("Clean, ATS-friendly formatting")
        if scores['length'] >= 85:
            strengths.append("Optimal letter length")
        if scores['action_verbs'] >= 80:
            strengths.append("Good use of action verbs")
        if scores['readability'] >= 85:
            strengths.append("Excellent readability")
        
        if not strengths:
            strengths.append("Letter structure is acceptable")
        
        return strengths
    
    def _identify_improvements(self, scores: Dict) -> List[str]:
        """Identify areas for improvement."""
        improvements = []
        
        if scores['keyword_match'] < 70:
            improvements.append("Include more keywords from the job description")
        if scores['formatting'] < 90:
            improvements.append("Simplify formatting for better ATS compatibility")
        if scores['length'] < 85:
            improvements.append("Adjust letter length to 250-400 words")
        if scores['action_verbs'] < 80:
            improvements.append("Use more strong action verbs to describe achievements")
        if scores['readability'] < 85:
            improvements.append("Adjust sentence length for better readability")
        
        if not improvements:
            improvements.append("Consider adding specific metrics and achievements")
        
        return improvements
    
    def suggest_keywords(self, job_description: str, current_letter: str) -> List[str]:
        """Suggest keywords to add based on job description."""
        job_words = set(re.findall(r'\b[a-zA-Z]{4,}\b', job_description.lower()))
        letter_words = set(re.findall(r'\b[a-zA-Z]{4,}\b', current_letter.lower()))
        
        stop_words = {'that', 'this', 'with', 'from', 'have', 'will', 'your', 
                      'their', 'about', 'which', 'where', 'when', 'what', 'these',
                      'those', 'them', 'they', 'than', 'then', 'there', 'here',
                      'must', 'should', 'would', 'could', 'also', 'well', 'very'}
        
        job_keywords = job_words - stop_words
        missing_keywords = job_keywords - letter_words
        
        # Return top 10 missing keywords
        return list(missing_keywords)[:10]
