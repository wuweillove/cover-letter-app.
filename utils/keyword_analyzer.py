import re
from collections import Counter
from typing import Dict, List

class KeywordAnalyzer:
    """Analyzes and extracts keywords from job descriptions and letters."""
    
    def __init__(self):
        self.stop_words = self._load_stop_words()
        self.technical_terms = self._load_technical_terms()
    
    def _load_stop_words(self) -> set:
        """Load common stop words to filter out."""
        return {
            'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
            'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
            'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she',
            'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their',
            'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go',
            'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know',
            'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them',
            'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over',
            'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first',
            'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day',
            'most', 'us', 'must', 'should', 'very', 'such', 'here', 'through', 'where'
        }
    
    def _load_technical_terms(self) -> Dict[str, List[str]]:
        """Load domain-specific technical terms."""
        return {
            'technology': [
                'python', 'java', 'javascript', 'react', 'angular', 'vue', 'node',
                'docker', 'kubernetes', 'aws', 'azure', 'gcp', 'sql', 'nosql',
                'api', 'rest', 'graphql', 'microservices', 'agile', 'scrum',
                'devops', 'ci/cd', 'git', 'jenkins', 'terraform', 'ansible'
            ],
            'finance': [
                'financial', 'analysis', 'modeling', 'valuation', 'portfolio',
                'risk', 'compliance', 'audit', 'gaap', 'ifrs', 'sox', 'cfa',
                'derivatives', 'equity', 'fixed income', 'hedge', 'trading'
            ],
            'marketing': [
                'seo', 'sem', 'ppc', 'roi', 'analytics', 'conversion', 'funnel',
                'campaign', 'brand', 'content', 'social media', 'engagement',
                'growth', 'acquisition', 'retention', 'crm', 'automation'
            ],
            'healthcare': [
                'patient', 'clinical', 'diagnosis', 'treatment', 'care',
                'medical', 'nursing', 'healthcare', 'ehr', 'hipaa',
                'pharmacology', 'therapy', 'procedure', 'assessment'
            ]
        }
    
    def extract_keywords(self, text: str, max_keywords: int = 20) -> List[Dict]:
        """Extract important keywords from text."""
        # Tokenize and clean
        words = re.findall(r'\b[a-zA-Z][a-zA-Z-]*\b', text.lower())
        
        # Filter stop words and short words
        filtered_words = [
            word for word in words 
            if word not in self.stop_words and len(word) > 3
        ]
        
        # Count frequency
        word_freq = Counter(filtered_words)
        
        # Get top keywords
        top_keywords = word_freq.most_common(max_keywords)
        
        # Format results
        return [
            {'word': word, 'frequency': freq, 'importance': self._calculate_importance(word, freq)}
            for word, freq in top_keywords
        ]
    
    def _calculate_importance(self, word: str, frequency: int) -> float:
        """Calculate importance score for a keyword."""
        # Base score from frequency
        score = frequency * 10
        
        # Boost for technical terms
        for domain, terms in self.technical_terms.items():
            if word in terms:
                score *= 1.5
                break
        
        # Boost for longer words (usually more specific)
        if len(word) > 8:
            score *= 1.2
        
        return round(score, 2)
    
    def analyze(self, letter: str, job_description: str) -> Dict:
        """Comprehensive keyword analysis."""
        job_keywords = self.extract_keywords(job_description, 30)
        letter_keywords = self.extract_keywords(letter, 30)
        
        # Extract just the words
        job_words = {kw['word'] for kw in job_keywords}
        letter_words = {kw['word'] for kw in letter_keywords}
        
        # Find matches and misses
        matched = job_words & letter_words
        missing = job_words - letter_words
        
        # Calculate coverage
        coverage = int((len(matched) / len(job_words) * 100)) if job_words else 0
        
        return {
            'coverage': coverage,
            'matched': sorted(list(matched))[:15],
            'missing': sorted(list(missing))[:10],
            'job_keywords': job_keywords[:10],
            'letter_keywords': letter_keywords[:10],
            'suggestions': self._generate_suggestions(matched, missing)
        }
    
    def _generate_suggestions(self, matched: set, missing: set) -> List[str]:
        """Generate actionable suggestions."""
        suggestions = []
        
        if len(matched) < 5:
            suggestions.append("Add more keywords from the job description to improve ATS match")
        
        if missing:
            top_missing = list(missing)[:3]
            suggestions.append(f"Consider incorporating: {', '.join(top_missing)}")
        
        if len(matched) >= 10:
            suggestions.append("Great keyword coverage! Focus on natural integration.")
        
        return suggestions
    
    def get_keyword_density(self, text: str, keyword: str) -> float:
        """Calculate density of a specific keyword."""
        words = text.lower().split()
        if not words:
            return 0.0
        
        count = words.count(keyword.lower())
        density = (count / len(words)) * 100
        return round(density, 2)
    
    def suggest_keyword_placement(self, letter: str, keywords: List[str]) -> Dict:
        """Suggest where to place missing keywords."""
        paragraphs = letter.split('\n\n')
        
        suggestions = {}
        for i, para in enumerate(paragraphs):
            para_lower = para.lower()
            missing_in_para = [kw for kw in keywords if kw not in para_lower]
            
            if missing_in_para:
                section = self._identify_section(i, len(paragraphs))
                suggestions[section] = missing_in_para[:3]
        
        return suggestions
    
    def _identify_section(self, index: int, total: int) -> str:
        """Identify which section of the letter based on paragraph index."""
        if index == 0:
            return "Opening"
        elif index == total - 1:
            return "Closing"
        else:
            return f"Body Paragraph {index}"
