# Contributing to Cover Letter Pro

First off, thank you for considering contributing to Cover Letter Pro! It's people like you that make this tool better for everyone. 🎉

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (screenshots, code snippets)
- **Describe the behavior you observed and what you expected**
- **Include your environment details** (OS, Python version, browser)

**Bug Report Template:**
```markdown
**Description:**
A clear description of what the bug is.

**To Reproduce:**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior:**
What you expected to happen.

**Screenshots:**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Windows 10, macOS 13]
- Python Version: [e.g., 3.9.0]
- Browser: [e.g., Chrome 120]
- Streamlit Version: [e.g., 1.28.0]

**Additional Context:**
Any other relevant information.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **Include mockups or examples if applicable**

**Enhancement Template:**
```markdown
**Feature Description:**
A clear description of the feature.

**Problem It Solves:**
What problem does this solve for users?

**Proposed Solution:**
How should this feature work?

**Alternatives Considered:**
What other solutions did you consider?

**Additional Context:**
Mockups, examples, or relevant information.
```

### Pull Requests

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/AmazingFeature
   ```

2. **Make your changes** following our coding standards

3. **Test your changes thoroughly**
   - Test all affected features
   - Ensure no existing functionality breaks
   - Test on different browsers if UI changes

4. **Update documentation** if needed
   - Update README.md for new features
   - Add docstrings to new functions
   - Update CHANGELOG.md

5. **Commit your changes** with clear messages
   ```bash
   git commit -m 'feat: Add amazing new feature'
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/AmazingFeature
   ```

7. **Open a Pull Request** with a clear title and description

## Development Setup

### Prerequisites
- Python 3.8+
- pip
- Virtual environment tool (venv or virtualenv)
- Git

### Setting Up Your Development Environment

1. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/cover-letter-app..git
   cd cover-letter-app.
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up secrets**
   ```bash
   mkdir -p .streamlit
   echo 'GOOGLE_API_KEY = "your-test-api-key"' > .streamlit/secrets.toml
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

### Project Structure

```
cover-letter-app./
├── app.py                      # Main application file
├── requirements.txt            # Python dependencies
├── .streamlit/
│   ├── config.toml            # Streamlit configuration
│   └── secrets.toml           # API keys (not in git)
├── .gitignore                 # Git ignore rules
├── README.md                  # Main documentation
├── CONTRIBUTING.md            # This file
└── CHANGELOG.md               # Version history
```

## Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

- **Line length**: 100 characters max
- **Imports**: Grouped (standard library, third-party, local)
- **Naming**:
  - Functions: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
  - Private: `_leading_underscore`

### Code Quality

- **Type Hints**: Use type hints for function parameters and returns
  ```python
  def sanitize_input(text: str) -> str:
      """Sanitize user input."""
      return text.strip()
  ```

- **Docstrings**: Use for all public functions
  ```python
  def extract_keywords(text: str, top_n: int = 10) -> List[str]:
      """
      Extract important keywords from text.
      
      Args:
          text: Input text to analyze
          top_n: Number of top keywords to return
          
      Returns:
          List of extracted keywords
      """
      pass
  ```

- **Comments**: Use for complex logic, not obvious code
  ```python
  # Good
  # Calculate exponential backoff for retry logic
  time.sleep(2 ** attempt)
  
  # Bad
  # Increment i by 1
  i += 1
  ```

### Git Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, no logic change)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

**Examples:**
```bash
feat: Add PDF export functionality
fix: Resolve rate limiting issue with API calls
docs: Update installation instructions in README
style: Format code according to PEP 8
refactor: Simplify keyword extraction logic
test: Add unit tests for input validation
chore: Update dependencies to latest versions
```

## Testing Guidelines

### Manual Testing Checklist

Before submitting a PR, test the following:

- [ ] Resume input accepts and displays text correctly
- [ ] Job description input accepts and displays text correctly
- [ ] Character counters update in real-time
- [ ] All tone options work correctly
- [ ] Letter generation completes successfully
- [ ] Generated letter is editable
- [ ] Download functionality works
- [ ] History saves and loads correctly
- [ ] Draft saving works
- [ ] Keywords are extracted and displayed
- [ ] Error messages display properly
- [ ] Rate limiting works as expected
- [ ] All sidebar options function correctly

### Browser Testing

Test on at least:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (Chrome/Safari)

### Feature Testing

When adding new features:
1. Test the happy path (everything works correctly)
2. Test edge cases (empty inputs, very long inputs)
3. Test error conditions (API failures, network issues)
4. Test with different user scenarios

## Areas That Need Contribution

### High Priority
- [ ] PDF export functionality
- [ ] DOCX export functionality
- [ ] Multiple AI model support (Claude, GPT-4)
- [ ] User authentication and saved profiles
- [ ] Email integration for direct sending
- [ ] Resume parsing and analysis

### Medium Priority
- [ ] Cover letter templates library
- [ ] Grammar and spell checking
- [ ] Translation to other languages
- [ ] ATS score calculator
- [ ] Dark mode implementation
- [ ] Mobile app version

### Low Priority
- [ ] Social media sharing
- [ ] Integration with job boards
- [ ] Chrome extension
- [ ] Analytics dashboard
- [ ] A/B testing for different approaches

## Documentation

### Code Documentation
- Add docstrings to all public functions
- Include type hints
- Comment complex algorithms
- Keep comments up-to-date with code changes

### User Documentation
- Update README.md for new features
- Add screenshots for UI changes
- Update usage guide for new workflows
- Create video tutorials if applicable

## Review Process

### Pull Request Review

Your PR will be reviewed for:
1. **Functionality**: Does it work as intended?
2. **Code Quality**: Is it clean, readable, and well-structured?
3. **Testing**: Has it been tested thoroughly?
4. **Documentation**: Is it properly documented?
5. **Compatibility**: Does it work with existing features?

### Review Timeline
- Initial review: Within 3-5 days
- Follow-up reviews: Within 2 days
- Merge: After approval and all checks pass

## Questions?

Don't hesitate to ask questions! You can:
- Open an issue with the `question` label
- Start a discussion in GitHub Discussions
- Comment on existing issues or PRs

## Recognition

Contributors will be:
- Listed in the README acknowledgments
- Mentioned in release notes
- Credited in commit history

Thank you for contributing to Cover Letter Pro! 🎉

---

**Happy Coding!** 💻
