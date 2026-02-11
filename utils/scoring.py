from typing import Dict, List
import re

class LetterScorer:
    """Score cover letter effectiveness and provide improvement suggestions."""
    
    def __init__(self):
        self.scoring_criteria = self._load_scoring_criteria()
    
    def _load_scoring_criteria(self) -> Dict:
        """Load scoring criteria weights."""
        return {
            'ats_score': 0.30,
            'grammar_score': 0.20,
            'keyword_coverage': 0.20,
            'structure': 0.15,
            'personalization': 0.15
        }
    
    def calculate_score(self, letter: str, ats_score: int, 
                       grammar_score: int, keyword_score: int) -> Dict:
        """Calculate overall effectiveness score."""
        
        # Calculate component scores
        structure_score = self._score_structure(letter)
        personalization_score = self._score_personalization(letter)
        
        # Weighted average
        total_score = (
            ats_score * self.scoring_criteria['ats_score'] +
            grammar_score * self.scoring_criteria['grammar_score'] +
            keyword_score * self.scoring_criteria['keyword_coverage'] +
            structure_score * self.scoring_criteria['structure'] +
            personalization_score * self.scoring_criteria['personalization']
        )
        
        return {
            'total': int(total_score),
            'ats': ats_score,
            'grammar': grammar_score,
            'keywords': keyword_score,
            'structure': structure_score,
            'personalization': personalization_score,
            'grade': self._get_grade(int(total_score)),
            'effectiveness': self._get_effectiveness_level(int(total_score))
        }
    
    def _score_structure(self, letter: str) -> int:
        """Score letter structure."""
        score = 100
        
        # Check paragraph count
        paragraphs = [p for p in letter.split('\n\n') if p.strip()]
        if len(paragraphs) < 3:
            score -= 20
        elif len(paragraphs) > 5:
            score -= 10
        
        # Check for clear opening
        if paragraphs:
            first_para = paragraphs[0].lower()
            if not any(word in first_para for word in ['position', 'role', 'opportunity', 'writing', 'apply']):
                score -= 15
        
        # Check for clear closing
        if paragraphs:
            last_para = paragraphs[-1].lower()
            if not any(word in last_para for word in ['thank', 'look forward', 'discuss', 'interview', 'contact']):
                score -= 15
        
        # Check word count
        word_count = len(letter.split())
        if not (200 <= word_count <= 500):
            score -= 15
        
        return max(score, 0)
    
    def _score_personalization(self, letter: str) -> int:
        """Score personalization and specificity."""
        score = 100
        letter_lower = letter.lower()
        
        # Check for generic phrases (negative indicators)
        generic_phrases = [
            'to whom it may concern',
            'dear sir or madam',
            'dear hiring manager',
            'i am writing to apply',
            'i am a hard worker',
            'team player',
            'detail-oriented'
        ]
        
        generic_count = sum(1 for phrase in generic_phrases if phrase in letter_lower)
        score -= (generic_count * 10)
        
        # Check for specific indicators (positive)
        has_company_name = bool(re.search(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', letter))
        has_numbers = bool(re.search(r'\d+%|\d+', letter))
        has_specific_role = len(re.findall(r'\b(?:role|position|opportunity)\b', letter_lower)) > 0
        
        if has_company_name:
            score += 0
        else:
            score -= 20
        
        if has_numbers:
            score += 0
        else:
            score -= 15
        
        if has_specific_role:
            score += 0
        else:
            score -= 10
        
        return max(min(score, 100), 0)
    
    def _get_grade(self, score: int) -> str:
        """Convert score to letter grade."""
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    def _get_effectiveness_level(self, score: int) -> str:
        """Get effectiveness description."""
        if score >= 90:
            return 'Exceptional - Very likely to impress recruiters'
        elif score >= 80:
            return 'Excellent - Strong chance of getting interview'
        elif score >= 70:
            return 'Good - Competitive application'
        elif score >= 60:
            return 'Fair - Needs some improvements'
        else:
            return 'Needs Work - Requires significant revision'
    
    def get_suggestions(self, letter: str, scores: Dict) -> List[Dict]:
        """Generate improvement suggestions based on scores."""
        suggestions = []
        
        # ATS suggestions
        if scores.get('ats', 0) < 80:
            suggestions.append({
                'title': 'Improve ATS Compatibility',
                'description': 'Your letter may not pass automated screening. Add more keywords from the job description and use standard formatting.',
                'priority': 'high',
                'example': 'Review the job posting and naturally incorporate key terms like required skills, qualifications, and technologies.'
            })
        
        # Grammar suggestions
        if scores.get('grammar', 0) < 80:
            suggestions.append({
                'title': 'Fix Grammar and Style Issues',
                'description': 'There are grammar or style issues that could hurt your credibility. Review and correct them.',
                'priority': 'high',
                'example': 'Use our grammar checker to identify and fix specific issues.'
            })
        
        # Keyword suggestions
        if scores.get('keywords', 0) < 70:
            suggestions.append({
                'title': 'Add More Relevant Keywords',
                'description': 'Your letter is missing important keywords from the job description.',
                'priority': 'high',
                'example': 'Review the "Missing Keywords" section and naturally incorporate them into your letter.'
            })
        
        # Structure suggestions
        if scores.get('structure', 0) < 75:
            suggestions.append({
                'title': 'Improve Letter Structure',
                'description': 'Your letter structure could be clearer. Use 3-4 distinct paragraphs.',
                'priority': 'medium',
                'example': 'Paragraph 1: Opening with enthusiasm\nParagraph 2-3: Relevant experience and achievements\nParagraph 4: Strong closing with call to action'
            })
        
        # Personalization suggestions
        if scores.get('personalization', 0) < 70:
            suggestions.append({
                'title': 'Make It More Personal and Specific',
                'description': 'Your letter feels generic. Add specific details about the company and role.',
                'priority': 'high',
                'example': 'Research the company and mention: specific products/projects, company values, recent news, or why you\'re excited about THIS role at THIS company.'
            })
        
        # Add quantification suggestion
        if not re.search(r'\d+%|\d+', letter):
            suggestions.append({
                'title': 'Add Quantifiable Achievements',
                'description': 'Include specific numbers, percentages, or metrics to demonstrate impact.',
                'priority': 'medium',
                'example': 'Instead of "improved performance", say "improved performance by 35%" or "led team of 8 engineers"'
            })
        
        # Check for passive voice
        passive_count = len(re.findall(r'\b(?:was|were|been|is|are)\s+\w+ed\b', letter))
        if passive_count > 3:
            suggestions.append({
                'title': 'Use More Active Voice',
                'description': f'Found {passive_count} instances of passive voice. Active voice is more engaging.',
                'priority': 'low',
                'example': 'Change "The project was completed by me" to "I completed the project"'
            })
        
        return suggestions
    
    def compare_versions(self, versions: List[Dict]) -> Dict:
        """Compare multiple letter versions and recommend the best."""
        if not versions:
            return {}
        
        comparison = []
        for i, version in enumerate(versions):
            score = self.calculate_score(
                version['content'],
                version.get('ats_score', 75),
                version.get('grammar_score', 85),
                version.get('keyword_score', 70)
            )
            comparison.append({
                'version': i + 1,
                'score': score['total'],
                'strengths': self._identify_version_strengths(version['content']),
                'weaknesses': self._identify_version_weaknesses(version['content'])
            })
        
        # Sort by score
        comparison.sort(key=lambda x: x['score'], reverse=True)
        
        return {
            'rankings': comparison,
            'recommended': comparison[0]['version'],
            'recommendation_reason': f"Version {comparison[0]['version']} has the highest overall score ({comparison[0]['score']}) with strong {', '.join(comparison[0]['strengths'][:2])}"
        }
    
    def _identify_version_strengths(self, letter: str) -> List[str]:
        """Identify strengths of a letter version."""
        strengths = []
        
        if len(re.findall(r'\d+%', letter)) >= 2:
            strengths.append('quantifiable achievements')
        
        if len(letter.split()) >= 300:
            strengths.append('comprehensive coverage')
        
        paragraphs = letter.split('\n\n')
        if len(paragraphs) == 4:
            strengths.append('well-structured')
        
        if len(re.findall(r'\b(?:achieved|developed|led|managed|created)\b', letter.lower())) >= 3:
            strengths.append('strong action verbs')
        
        return strengths if strengths else ['acceptable format']
    
    def _identify_version_weaknesses(self, letter: str) -> List[str]:
        """Identify weaknesses of a letter version."""
        weaknesses = []
        
        if not re.search(r'\d+', letter):
            weaknesses.append('lacks specific metrics')
        
        if len(letter.split()) < 250:
            weaknesses.append('too brief')
        elif len(letter.split()) > 450:
            weaknesses.append('too lengthy')
        
        if 'I am a' in letter or 'I am very' in letter:
            weaknesses.append('generic phrasing')
        
        return weaknesses if weaknesses else ['minor improvements possible']
