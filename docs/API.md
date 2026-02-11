# API Documentation

This document provides technical details about the internal API and functions used in Cover Letter Pro.

## Table of Contents
- [Core Functions](#core-functions)
- [Helper Functions](#helper-functions)
- [Configuration](#configuration)
- [Session State](#session-state)
- [Error Handling](#error-handling)

---

## Core Functions

### `generate_cover_letter()`

Generates a cover letter using AI with comprehensive error handling.

**Signature:**
```python
def generate_cover_letter(
    resume: str, 
    job: str, 
    tone: str, 
    length: int,
    emphasis_areas: List[str]
) -> Optional[str]
```

**Parameters:**
- `resume` (str): The user's resume or work experience
- `job` (str): The job description
- `tone` (str): Selected tone from TONE_PROFILES keys
- `length` (int): Target word count for the letter
- `emphasis_areas` (List[str]): Areas to emphasize in the letter

**Returns:**
- `str`: Generated cover letter text
- `None`: If generation fails

**Raises:**
- Catches all exceptions internally and returns None

**Example:**
```python
letter = generate_cover_letter(
    resume="Software Engineer with 5 years...",
    job="Looking for Senior Developer...",
    tone="Professional & Formal",
    length=350,
    emphasis_areas=["Technical Skills", "Leadership"]
)
```

**Implementation Details:**
- Extracts keywords from job description
- Creates enhanced prompt using `create_enhanced_prompt()`
- Implements retry logic with exponential backoff (3 attempts)
- Uses Google Gemini 1.5 Flash model
- Configured with temperature=0.7, top_p=0.9, top_k=40

---

## Helper Functions

### `sanitize_input()`

Removes potentially harmful characters from user input.

**Signature:**
```python
def sanitize_input(text: str) -> str
```

**Parameters:**
- `text` (str): Raw user input

**Returns:**
- `str`: Sanitized text with harmful characters removed

**Security:**
- Removes: `< > { }`
- Preserves: Formatting and whitespace
- Strips leading/trailing whitespace

**Example:**
```python
safe_text = sanitize_input("<script>alert('xss')</script>Hello")
# Returns: "scriptalert('xss')/scriptHello"
```

---

### `extract_keywords()`

Extracts important keywords from job descriptions for ATS optimization.

**Signature:**
```python
def extract_keywords(text: str, top_n: int = 10) -> List[str]
```

**Parameters:**
- `text` (str): Job description text
- `top_n` (int): Number of keywords to return (default: 10)

**Returns:**
- `List[str]`: List of extracted keywords, sorted by frequency

**Algorithm:**
1. Tokenize text (words 4+ characters)
2. Convert to lowercase
3. Remove stop words
4. Count frequency
5. Return top N most frequent

**Stop Words:**
```python
stop_words = {
    'that', 'this', 'with', 'from', 'have', 
    'will', 'your', 'their', 'would', 'about', 
    'which', 'there', 'other'
}
```

**Example:**
```python
keywords = extract_keywords("Python developer with React experience...", 5)
# Returns: ['python', 'developer', 'react', 'experience', ...]
```

---

### `validate_inputs()`

Validates user inputs for completeness and length requirements.

**Signature:**
```python
def validate_inputs(resume: str, job: str) -> tuple[bool, str]
```

**Parameters:**
- `resume` (str): Resume text to validate
- `job` (str): Job description to validate

**Returns:**
- `tuple[bool, str]`: (is_valid, error_message)
  - `(True, "")` if valid
  - `(False, "error message")` if invalid

**Validation Rules:**
- Resume: Not empty, ≥100 chars, ≤5000 chars
- Job: Not empty, ≥50 chars, ≤5000 chars

**Example:**
```python
is_valid, error = validate_inputs("My resume...", "Job description...")
if not is_valid:
    print(f"Error: {error}")
```

---

### `create_enhanced_prompt()`

Creates a structured, detailed prompt for the AI model.

**Signature:**
```python
def create_enhanced_prompt(
    resume: str,
    job: str,
    tone: str,
    length: int,
    keywords: List[str],
    emphasis_areas: List[str]
) -> str
```

**Parameters:**
- `resume` (str): User's resume
- `job` (str): Job description
- `tone` (str): Selected tone
- `length` (int): Target word count
- `keywords` (List[str]): Extracted keywords to incorporate
- `emphasis_areas` (List[str]): Areas to emphasize

**Returns:**
- `str`: Complete prompt for AI model

**Prompt Structure:**
1. Role definition (professional cover letter writer)
2. Task description
3. Tone and style requirements
4. Target length
5. Structure requirements (opening, body, closing)
6. Emphasis areas
7. Formatting guidelines
8. Key requirements (ATS-friendly, specific, etc.)
9. Input data (resume and job description)

**Example:**
```python
prompt = create_enhanced_prompt(
    resume="...",
    job="...",
    tone="Professional & Formal",
    length=350,
    keywords=["python", "leadership"],
    emphasis_areas=["Technical Skills"]
)
```

---

### `check_rate_limit()`

Implements simple rate limiting to prevent API abuse.

**Signature:**
```python
def check_rate_limit() -> bool
```

**Returns:**
- `bool`: True if request allowed, False if rate limited

**Configuration:**
- Cooldown: 10 seconds between requests (configurable via `RATE_LIMIT_SECONDS`)
- Storage: Session state (`last_generation_time`)

**Example:**
```python
if not check_rate_limit():
    st.warning("Please wait before generating again")
else:
    # Proceed with generation
    pass
```

---

### `create_txt_download()`

Creates a downloadable TXT file from string content.

**Signature:**
```python
def create_txt_download(content: str) -> BytesIO
```

**Parameters:**
- `content` (str): Text content for the file

**Returns:**
- `BytesIO`: In-memory bytes buffer ready for download

**Encoding:**
- UTF-8 encoding for international character support

**Example:**
```python
buffer = create_txt_download("My cover letter content...")
st.download_button(
    "Download",
    data=buffer,
    file_name="letter.txt",
    mime="text/plain"
)
```

---

## Configuration

### Constants

```python
# API Configuration
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# Character Limits
MAX_RESUME_CHARS = 5000
MAX_JOB_CHARS = 5000

# Rate Limiting
RATE_LIMIT_SECONDS = 10

# Donation Link
DONATION_LINK = "https://www.buymeacoffee.com/coverletter"
```

### Tone Profiles

```python
TONE_PROFILES = {
    "Professional & Formal": {
        "description": "Traditional corporate tone",
        "prompt_modifier": "formal, corporate language"
    },
    # ... additional tones
}
```

### Length Options

```python
LENGTH_OPTIONS = {
    "Concise (200-250 words)": 250,
    "Standard (300-350 words)": 350,
    "Detailed (400-500 words)": 500
}
```

---

## Session State

### State Variables

| Variable | Type | Purpose |
|----------|------|---------|
| `generated_letters` | `List[Dict]` | History of all generated letters |
| `current_letter` | `Optional[str]` | Currently displayed letter |
| `draft_resume` | `str` | Saved resume draft |
| `draft_job` | `str` | Saved job description draft |
| `last_generation_time` | `float` | Timestamp of last generation (for rate limiting) |

### Letter History Structure

```python
{
    'content': str,          # The generated letter text
    'timestamp': str,        # Format: "YYYY-MM-DD HH:MM:SS"
    'tone': str,            # Selected tone
    'length': str           # Length option label
}
```

### Accessing Session State

```python
# Initialize
if 'generated_letters' not in st.session_state:
    st.session_state.generated_letters = []

# Add to history
st.session_state.generated_letters.append({
    'content': letter_text,
    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'tone': tone,
    'length': length_label
})

# Access current letter
if st.session_state.current_letter:
    display_letter(st.session_state.current_letter)
```

---

## Error Handling

### Error Types

#### User Input Errors
```python
# Empty input
if not resume:
    st.error("Resume cannot be empty.")

# Too short
if len(resume) < 100:
    st.error("Resume seems too short. Please provide more details.")

# Too long
if len(resume) > MAX_RESUME_CHARS:
    st.error(f"Resume exceeds maximum length of {MAX_RESUME_CHARS} characters.")
```

#### API Errors
```python
try:
    response = model.generate_content(prompt)
except Exception as e:
    st.error(f"❌ Generation failed: {str(e)}")
    if "quota" in str(e).lower():
        st.error("⚠️ API quota exceeded. Please try again later.")
```

#### Rate Limiting
```python
if not check_rate_limit():
    st.warning(f"⏳ Please wait {RATE_LIMIT_SECONDS} seconds between generations.")
```

### Retry Logic

```python
max_retries = 3
for attempt in range(max_retries):
    try:
        result = generate_content()
        break
    except Exception as e:
        if attempt == max_retries - 1:
            raise
        time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s, 4s
```

---

## AI Model Configuration

### Gemini 1.5 Flash Settings

```python
model = genai.GenerativeModel('gemini-1.5-flash')

generation_config = genai.types.GenerationConfig(
    temperature=0.7,        # Creativity level (0-1)
    top_p=0.9,             # Nucleus sampling threshold
    top_k=40,              # Token selection diversity
    max_output_tokens=2048 # Maximum response length
)
```

### Parameter Explanations

- **temperature**: Controls randomness
  - 0 = Deterministic, consistent
  - 1 = Creative, varied
  - 0.7 = Balanced for professional writing

- **top_p**: Nucleus sampling
  - Considers top tokens totaling this probability
  - 0.9 = Good balance of quality and creativity

- **top_k**: Token selection
  - Limits to top K tokens
  - 40 = Sufficient variety without nonsense

- **max_output_tokens**: Length limit
  - 2048 = Enough for detailed cover letters

---

## Extension Points

### Adding New Tone Profiles

```python
TONE_PROFILES["Your Custom Tone"] = {
    "description": "Description for users",
    "prompt_modifier": "Instructions for AI"
}
```

### Adding New Emphasis Areas

```python
emphasis_areas = st.multiselect(
    "Focus on:",
    [
        "Existing options...",
        "Your New Option"  # Add here
    ]
)
```

### Changing AI Model

```python
# Replace model initialization
model = genai.GenerativeModel('gemini-1.5-pro')  # More capable
# or
model = genai.GenerativeModel('gemini-1.0-pro')  # More economical
```

---

## Performance Considerations

### Optimization Tips

1. **Keyword Extraction**
   - Current: O(n) simple frequency count
   - Enhancement: Use NLP library (spaCy, NLTK) for better extraction

2. **Session State**
   - Stored in browser memory
   - Cleared on page refresh
   - Consider adding export/import for persistence

3. **API Calls**
   - Cached: None currently
   - Enhancement: Cache similar requests

4. **Rate Limiting**
   - Current: Simple time-based
   - Enhancement: IP-based or token bucket algorithm

---

## Testing

### Unit Test Examples

```python
def test_sanitize_input():
    assert sanitize_input("<script>") == "script"
    assert sanitize_input("Hello{}") == "Hello"
    assert sanitize_input("  text  ") == "text"

def test_validate_inputs():
    # Valid inputs
    is_valid, _ = validate_inputs("x" * 100, "y" * 50)
    assert is_valid == True
    
    # Too short
    is_valid, msg = validate_inputs("short", "job")
    assert is_valid == False
    assert "too short" in msg.lower()

def test_extract_keywords():
    text = "python developer python react"
    keywords = extract_keywords(text, 2)
    assert "python" in keywords
    assert len(keywords) <= 2
```

---

## API Response Examples

### Successful Generation

```json
{
    "text": "[Your Name]\n[Email]...\n\nDear Hiring Manager...",
    "timestamp": "2026-02-11T02:45:00Z",
    "word_count": 342
}
```

### Error Response

```json
{
    "error": "API quota exceeded",
    "code": "RESOURCE_EXHAUSTED",
    "timestamp": "2026-02-11T02:45:00Z"
}
```

---

## Logging

### Server-Side Logging

```python
# Generation events
print(f"[{datetime.datetime.now()}] Letter generated - Tone: {tone}, Length: {length}")

# Error logging
logger.error(f"Generation failed: {error}")
```

### Client-Side Logging

- Browser console for debugging
- Session state for user actions
- No sensitive data logged

---

## Security Considerations

### Input Sanitization

All user inputs are sanitized before:
- Storing in session state
- Passing to AI model
- Displaying in UI

### API Key Protection

- Stored in `.streamlit/secrets.toml`
- Never exposed in client-side code
- Never logged or displayed

### Rate Limiting

- 10 second cooldown between requests
- Prevents abuse and excessive API costs
- Session-based tracking

---

## Further Reading

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

**Last Updated**: February 2026
