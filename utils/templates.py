class TemplateManager:
    """Manages industry-specific cover letter templates."""
    
    def __init__(self):
        self.industries = self._get_industry_list()
        self.templates = self._load_templates()
    
    def _get_industry_list(self):
        return [
            "Technology",
            "Finance & Banking",
            "Healthcare & Medical",
            "Education & Academia",
            "Marketing & Advertising",
            "Sales & Business Development",
            "Engineering & Manufacturing",
            "Legal & Compliance",
            "Design & Creative",
            "Hospitality & Service",
            "Real Estate",
            "Consulting",
            "Non-Profit & Social Services",
            "Government & Public Sector"
        ]
    
    def _load_templates(self):
        return {
            "Technology": [
                "Software Engineer - Modern",
                "Data Scientist - Analytics Focused",
                "Product Manager - Agile",
                "DevOps Engineer - Cloud Native",
                "Full Stack Developer - Startup",
                "Security Engineer - Compliance",
                "UX/UI Designer - User Centered"
            ],
            "Finance & Banking": [
                "Financial Analyst - Quantitative",
                "Investment Banker - Deal Focused",
                "Risk Manager - Regulatory",
                "Portfolio Manager - Client Focused",
                "Accountant - CPA Track"
            ],
            "Healthcare & Medical": [
                "Registered Nurse - Patient Care",
                "Physician - Specialist",
                "Healthcare Administrator",
                "Medical Researcher",
                "Pharmacist - Clinical"
            ],
            "Marketing & Advertising": [
                "Digital Marketing Manager",
                "Content Strategist",
                "Brand Manager",
                "Social Media Manager",
                "SEO Specialist"
            ],
            "Education & Academia": [
                "Teacher - K-12",
                "Professor - Research Focused",
                "Academic Administrator",
                "Curriculum Developer"
            ],
            "Sales & Business Development": [
                "Sales Executive - B2B",
                "Business Development Manager",
                "Account Manager - Enterprise",
                "Sales Engineer"
            ],
            "Engineering & Manufacturing": [
                "Mechanical Engineer",
                "Electrical Engineer",
                "Quality Assurance Engineer",
                "Manufacturing Manager"
            ],
            "Legal & Compliance": [
                "Attorney - Corporate",
                "Paralegal",
                "Compliance Officer",
                "Legal Counsel"
            ],
            "Design & Creative": [
                "Graphic Designer",
                "Art Director",
                "Creative Director",
                "Illustrator"
            ],
            "Consulting": [
                "Management Consultant",
                "Strategy Consultant",
                "IT Consultant",
                "HR Consultant"
            ]
        }
    
    def get_industries(self):
        """Get list of all industries."""
        return self.industries
    
    def get_templates_by_industry(self, industry):
        """Get templates for a specific industry."""
        return self.templates.get(industry, ["Standard Professional", "Modern", "Traditional"])
    
    def get_template_preview(self, template_name):
        """Get preview text for a template."""
        previews = {
            "Software Engineer - Modern": """
**Preview: Software Engineer - Modern Template**

This template emphasizes:
- Technical skills and frameworks
- Project impact with metrics
- Open-source contributions
- Modern development practices
- Team collaboration tools

Tone: Professional yet approachable
Length: Concise, focused on achievements
            """,
            "Financial Analyst - Quantitative": """
**Preview: Financial Analyst - Quantitative Template**

This template emphasizes:
- Analytical and quantitative skills
- Financial modeling experience
- Data-driven decision making
- Regulatory knowledge
- Risk assessment capabilities

Tone: Formal and precise
Length: Detailed with specific metrics
            """,
            "Digital Marketing Manager": """
**Preview: Digital Marketing Manager Template**

This template emphasizes:
- ROI and conversion metrics
- Multi-channel campaign experience
- Analytics and A/B testing
- Brand growth strategies
- Team leadership

Tone: Creative yet results-focused
Length: Balanced with achievements
            """
        }
        return previews.get(template_name, "Template preview not available. This template will be customized based on your inputs.")
    
    def get_template_structure(self, template_name):
        """Get structural guidelines for a template."""
        return {
            'paragraphs': 4,
            'opening_style': 'enthusiastic',
            'body_focus': ['experience', 'achievements', 'skills'],
            'closing_style': 'confident',
            'keywords_emphasis': 'high'
        }
