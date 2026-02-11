import re
from typing import Dict, List

class GrammarChecker:
    """Basic grammar and style checking for cover letters."""
    
    def __init__(self):
        self.common_mistakes = self._load_common_mistakes()
        self.style_rules = self._load_style_rules()
    
    def _load_common_mistakes(self) -> Dict:
        """Load common grammar mistakes to check for."""
        return {
            'their/there/they\'re': [
                (r'\btheir\b', 'their (possessive)'),
                (r'\bthere\b', 'there (location)'),
                (r'\bthey\'re\b', "they're (they are)")
            ],
            'its/it\'s': [
                (r'\bits\b', 'its (possessive)'),
                (r'\bit\'s\b', "it's (it is)")
            ],
            'affect/effect': [
                (r'\baffect\b', 'affect (verb)'),
                (r'\beffect\b', 'effect (noun)')
            ]
        }
    
    def _load_style_rules(self) -> List[Dict]:
        """Load style rules for professional writing."""
        return [
            {
                'name': 'Passive voice',
                'pattern': r'\b(is|are|was|were|been|be)\s+\w+ed\b',
                'severity': 'info',
                'suggestion': 'Consider using active voice for stronger impact'
            },
            {
                'name': 'Weak words',
                'pattern': r'\b(very|really|quite|rather|somewhat|fairly)\b',
                'severity': 'warning',
                'suggestion': 'Use more specific, powerful words'
            },
            {
                'name': 'Redundant phrases',
                'pattern': r'\b(in order to|due to the fact that|at this point in time)\b',
                'severity': 'info',
                'suggestion': 'Simplify: use "to", "because", "now"'
            },
            {
                'name': 'Clichés',
                'pattern': r'\b(team player|hard worker|detail-oriented|think outside the box|hit the ground running)\b',
                'severity': 'warning',
                'suggestion': 'Replace with specific examples and achievements'
            }
        ]
    
    def check(self, text: str) -> Dict:
        """Perform comprehensive grammar and style check."""
        issues = []
        
        # Check basic grammar
        issues.extend(self._check_spelling_basics(text))
        
        # Check style
        issues.extend(self._check_style(text))
        
        # Check sentence structure
        issues.extend(self._check_sentence_structure(text))
        
        # Check punctuation
        issues.extend(self._check_punctuation(text))
        
        # Calculate score
        score = self._calculate_grammar_score(text, issues)
        
        return {
            'score': score,
            'issues': issues[:10],  # Return top 10 issues
            'total_issues': len(issues),
            'summary': self._generate_summary(score, issues)
        }
    
    def _check_spelling_basics(self, text: str) -> List[Dict]:
        """Check for basic spelling issues."""
        issues = []
        
        # Check for repeated words
        pattern = r'\b(\w+)\s+\1\b'
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            issues.append({
                'type': 'spelling',
                'severity': 'error',
                'message': f"Repeated word: '{match.group(1)}'",
                'position': match.start()
            })
        
        return issues
    
    def _check_style(self, text: str) -> List[Dict]:
        """Check style rules."""
        issues = []
        
        for rule in self.style_rules:
            matches = re.finditer(rule['pattern'], text, re.IGNORECASE)
            for match in matches:
                issues.append({
                    'type': 'style',
                    'severity': rule['severity'],
                    'message': f"{rule['name']}: {rule['suggestion']}",
                    'position': match.start(),
                    'text': match.group(0)
                })
        
        return issues
    
    def _check_sentence_structure(self, text: str) -> List[Dict]:
        """Check sentence structure issues."""
        issues = []
        sentences = re.split(r'[.!?]\s+', text)
        
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            
            # Check sentence length
            if len(words) > 30:
                issues.append({
                    'type': 'structure',
                    'severity': 'warning',
                    'message': f"Sentence {i+1} is too long ({len(words)} words). Consider breaking it up.",
                    'position': text.find(sentence)
                })
            elif len(words) < 5 and len(words) > 0:
                issues.append({
                    'type': 'structure',
                    'severity': 'info',
                    'message': f"Sentence {i+1} is very short ({len(words)} words). Ensure it's complete.",
                    'position': text.find(sentence)
                })
            
            # Check for sentence starting with 'And', 'But', 'Or'
            if sentence.strip() and re.match(r'^(And|But|Or)\b', sentence.strip(), re.IGNORECASE):
                issues.append({
                    'type': 'structure',
                    'severity': 'info',
                    'message': f"Sentence {i+1} starts with conjunction. Consider rephrasing for formal writing.",
                    'position': text.find(sentence)
                })
        
        return issues
    
    def _check_punctuation(self, text: str) -> List[Dict]:
        """Check punctuation issues."""
        issues = []
        
        # Check for double spaces
        if '  ' in text:
            issues.append({
                'type': 'punctuation',
                'severity': 'info',
                'message': 'Double spaces found. Use single spaces.',
                'position': text.find('  ')
            })
        
        # Check for missing spaces after punctuation
        pattern = r'[.,!?]\w'
        matches = re.finditer(pattern, text)
        for match in matches:
            issues.append({
                'type': 'punctuation',
                'severity': 'warning',
                'message': 'Missing space after punctuation.',
                'position': match.start()
            })
        
        # Check for missing periods at end of sentences
        lines = text.strip().split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 20 and not re.search(r'[.!?:]$', line):
                issues.append({
                    'type': 'punctuation',
                    'severity': 'warning',
                    'message': 'Line may be missing end punctuation.',
                    'position': text.find(line)
                })
        
        return issues
    
    def _calculate_grammar_score(self, text: str, issues: List[Dict]) -> int:
        """Calculate overall grammar score."""
        if not text:
            return 0
        
        # Start with perfect score
        score = 100
        
        # Deduct points based on issue severity
        for issue in issues:
            if issue['severity'] == 'error':
                score -= 5
            elif issue['severity'] == 'warning':
                score -= 2
            elif issue['severity'] == 'info':
                score -= 1
        
        # Minimum score is 50
        return max(score, 50)
    
    def _generate_summary(self, score: int, issues: List[Dict]) -> str:
        """Generate summary of grammar check."""
        if score >= 90:
            return "Excellent! Your letter has minimal grammar and style issues."
        elif score >= 75:
            return "Good! A few minor issues to address."
        elif score >= 60:
            return "Fair. Several issues should be corrected before sending."
        else:
            return "Needs improvement. Review and correct the identified issues."
    
    def suggest_improvements(self, text: str) -> List[Dict]:
        """Suggest specific improvements for the text."""
        suggestions = []
        
        # Check for first-person pronouns
        i_count = len(re.findall(r'\bI\b', text))
        if i_count > 10:
            suggestions.append({
                'type': 'balance',
                'message': f"You used 'I' {i_count} times. Balance with company-focused language.",
                'example': 'Instead of "I achieved X", try "This achievement would help Company Y..."'
            })
        
        # Check for specific examples
        numbers = re.findall(r'\d+%|\d+', text)
        if len(numbers) < 2:
            suggestions.append({
                'type': 'specificity',
                'message': 'Add more quantifiable achievements (percentages, numbers, metrics).',
                'example': 'E.g., "Increased sales by 35%" or "Managed team of 12"'
            })
        
        # Check paragraph structure
        paragraphs = text.split('\n\n')
        if len(paragraphs) < 3:
            suggestions.append({
                'type': 'structure',
                'message': 'Consider breaking into 3-4 clear paragraphs for better readability.',
                'example': 'Opening, Experience/Skills (1-2 paras), Closing'
            })
        
        return suggestions
