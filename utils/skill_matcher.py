import re
from typing import Dict, List, Set

class SkillMatcher:
    """Matches skills between resume, job description, and cover letter."""
    
    def __init__(self):
        self.skill_categories = self._load_skill_categories()
    
    def _load_skill_categories(self) -> Dict[str, List[str]]:
        """Load categorized skill keywords."""
        return {
            'technical': [
                'python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php', 'swift',
                'react', 'angular', 'vue', 'node.js', 'django', 'flask', 'spring',
                'sql', 'postgresql', 'mysql', 'mongodb', 'redis', 'elasticsearch',
                'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'git',
                'tensorflow', 'pytorch', 'scikit-learn', 'pandas', 'numpy',
                'rest api', 'graphql', 'microservices', 'agile', 'scrum'
            ],
            'soft_skills': [
                'leadership', 'communication', 'teamwork', 'problem-solving',
                'critical thinking', 'creativity', 'adaptability', 'time management',
                'collaboration', 'negotiation', 'presentation', 'mentoring',
                'conflict resolution', 'decision making', 'emotional intelligence'
            ],
            'management': [
                'project management', 'team leadership', 'strategic planning',
                'budget management', 'stakeholder management', 'resource allocation',
                'risk management', 'change management', 'vendor management',
                'agile methodology', 'scrum master', 'product management'
            ],
            'analytical': [
                'data analysis', 'statistical analysis', 'business intelligence',
                'financial modeling', 'forecasting', 'market research',
                'a/b testing', 'metrics analysis', 'kpi tracking', 'reporting'
            ],
            'creative': [
                'graphic design', 'ui/ux design', 'content creation', 'copywriting',
                'brand development', 'video editing', 'photography', 'illustration',
                'storytelling', 'creative direction'
            ],
            'domain_specific': [
                'compliance', 'regulatory', 'quality assurance', 'customer service',
                'sales', 'marketing', 'operations', 'finance', 'accounting',
                'human resources', 'legal', 'healthcare', 'education', 'research'
            ]
        }
    
    def extract_skills(self, text: str) -> Dict[str, List[str]]:
        """Extract skills from text, categorized."""
        text_lower = text.lower()
        found_skills = {category: [] for category in self.skill_categories}
        
        for category, skills in self.skill_categories.items():
            for skill in skills:
                # Check for exact match or as part of phrase
                pattern = r'\b' + re.escape(skill) + r'\b'
                if re.search(pattern, text_lower):
                    found_skills[category].append(skill)
        
        return {k: v for k, v in found_skills.items() if v}  # Remove empty categories
    
    def match_skills(self, resume: str, job_description: str, letter: str) -> Dict:
        """Match skills across resume, job description, and cover letter."""
        # Extract skills from each source
        resume_skills = self.extract_skills(resume)
        job_skills = self.extract_skills(job_description)
        letter_skills = self.extract_skills(letter)
        
        # Flatten to sets for comparison
        resume_set = self._flatten_skills(resume_skills)
        job_set = self._flatten_skills(job_skills)
        letter_set = self._flatten_skills(letter_skills)
        
        # Calculate matches
        matched_skills = job_set & letter_set
        missing_in_letter = job_set - letter_set
        available_in_resume = missing_in_letter & resume_set
        
        # Calculate match percentage
        match_percentage = int((len(matched_skills) / len(job_set) * 100)) if job_set else 0
        
        return {
            'match_percentage': match_percentage,
            'matched_skills': sorted(list(matched_skills))[:15],
            'missing_skills': sorted(list(missing_in_letter))[:10],
            'suggested_from_resume': sorted(list(available_in_resume))[:8],
            'by_category': self._categorize_matches(matched_skills, missing_in_letter),
            'recommendations': self._generate_recommendations(
                match_percentage, 
                matched_skills, 
                missing_in_letter,
                available_in_resume
            )
        }
    
    def _flatten_skills(self, categorized_skills: Dict[str, List[str]]) -> Set[str]:
        """Flatten categorized skills into a single set."""
        return {skill for skills in categorized_skills.values() for skill in skills}
    
    def _categorize_matches(self, matched: Set[str], missing: Set[str]) -> Dict:
        """Categorize matched and missing skills."""
        result = {}
        
        for category, skills in self.skill_categories.items():
            category_matched = [s for s in matched if s in skills]
            category_missing = [s for s in missing if s in skills]
            
            if category_matched or category_missing:
                result[category] = {
                    'matched': category_matched,
                    'missing': category_missing
                }
        
        return result
    
    def _generate_recommendations(self, match_percentage: int, 
                                  matched: Set[str], missing: Set[str],
                                  available: Set[str]) -> List[str]:
        """Generate actionable recommendations."""
        recommendations = []
        
        if match_percentage >= 80:
            recommendations.append("✅ Excellent skill coverage! Your letter highlights most required skills.")
        elif match_percentage >= 60:
            recommendations.append("✓ Good skill coverage, but consider adding a few more key skills.")
        else:
            recommendations.append("⚠️ Low skill coverage. Add more relevant skills from the job description.")
        
        if available:
            top_available = list(available)[:3]
            recommendations.append(
                f"💡 You have these skills in your resume but haven't mentioned them in the letter: "
                f"{', '.join(top_available)}"
            )
        
        if missing and not available:
            recommendations.append(
                "📚 Consider acquiring or highlighting transferable skills related to: "
                f"{', '.join(list(missing)[:3])}"
            )
        
        if len(matched) > 10:
            recommendations.append(
                "🎯 Great! You're highlighting a diverse range of relevant skills."
            )
        
        return recommendations
    
    def get_skill_gaps(self, resume: str, job_description: str) -> Dict:
        """Identify skill gaps between resume and job requirements."""
        resume_skills = self._flatten_skills(self.extract_skills(resume))
        job_skills = self._flatten_skills(self.extract_skills(job_description))
        
        gaps = job_skills - resume_skills
        overlap = job_skills & resume_skills
        
        gap_percentage = int((len(gaps) / len(job_skills) * 100)) if job_skills else 0
        
        return {
            'gap_percentage': gap_percentage,
            'matching_skills': sorted(list(overlap)),
            'missing_skills': sorted(list(gaps)),
            'total_required': len(job_skills),
            'total_matching': len(overlap)
        }
    
    def suggest_skill_phrasing(self, skill: str) -> List[str]:
        """Suggest different ways to phrase a skill."""
        phrasing_map = {
            'python': ['Python programming', 'Python development', 'proficient in Python'],
            'leadership': ['team leadership', 'leading teams', 'leadership experience'],
            'project management': ['managing projects', 'project coordination', 'project leadership'],
            'communication': ['strong communication skills', 'effective communicator', 'communication abilities'],
            'data analysis': ['analyzing data', 'data analytics', 'analytical skills']
        }
        
        return phrasing_map.get(skill.lower(), [f"experience with {skill}", f"{skill} expertise"])
