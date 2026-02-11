# Security Policy

## Supported Versions

We release security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.0.x   | :x:                |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

### 🔒 Private Disclosure

**DO NOT** open a public issue for security vulnerabilities.

Instead:

1. **Email us directly** at the repository owner's email (check GitHub profile)
2. **Include the following information:**
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)
   - Your contact information

### 📋 What to Expect

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 5 business days
- **Fix Timeline**: Depends on severity
  - Critical: Within 7 days
  - High: Within 14 days
  - Medium: Within 30 days
  - Low: Next regular release

### 🏆 Recognition

- Security researchers who responsibly disclose vulnerabilities will be acknowledged in:
  - SECURITY.md (this file)
  - Release notes
  - README.md (Hall of Fame section)

## Security Best Practices

### For Users

#### Protecting Your API Keys

1. **Never commit API keys to version control**
   ```bash
   # Always in .gitignore
   .streamlit/secrets.toml
   .env
   ```

2. **Use environment variables or secrets management**
   - Streamlit Cloud: Use Secrets management
   - Heroku: Use Config Vars
   - Docker: Use environment variables
   - Self-hosted: Use systemd environment files

3. **Rotate keys regularly**
   - Every 90 days minimum
   - Immediately if compromised
   - After team member departure

4. **Use restricted API keys**
   - Limit to specific services
   - Set quota limits
   - Enable IP restrictions if possible

#### Input Safety

1. **Don't paste sensitive personal information**
   - SSN, credit card numbers
   - Passwords or credentials
   - Private medical information

2. **Review generated content**
   - AI can make mistakes
   - Always customize for the specific job
   - Remove any unintended information

3. **Clear browser data**
   - Session data is stored in browser
   - Clear cache to remove history
   - Use private/incognito mode for sensitive applications

### For Developers

#### Code Security

1. **Input Validation**
   ```python
   # Always validate and sanitize inputs
   def sanitize_input(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r'[<>{}]', '', text)
       return text.strip()
   ```

2. **Rate Limiting**
   ```python
   # Implement rate limiting
   RATE_LIMIT_SECONDS = 10
   if time.time() - last_request < RATE_LIMIT_SECONDS:
       raise RateLimitError()
   ```

3. **Error Handling**
   ```python
   # Don't expose sensitive info in errors
   try:
       result = api_call()
   except Exception as e:
       # Log detailed error server-side
       logger.error(f"API Error: {e}")
       # Show generic message to user
       raise UserFriendlyError("Generation failed. Please try again.")
   ```

4. **Dependencies**
   ```bash
   # Keep dependencies updated
   pip list --outdated
   pip install --upgrade package-name
   ```

#### API Security

1. **Key Management**
   - Never hardcode API keys
   - Use secrets management systems
   - Implement key rotation
   - Monitor API usage

2. **Request Validation**
   - Validate all inputs
   - Implement request signing
   - Use HTTPS only
   - Set appropriate timeouts

3. **Response Handling**
   - Validate API responses
   - Handle errors gracefully
   - Don't log sensitive data
   - Implement retry logic

#### Deployment Security

1. **HTTPS Only**
   - Always use SSL/TLS
   - Use Let's Encrypt for free certificates
   - Configure HSTS headers

2. **Security Headers**
   ```python
   # In Streamlit config.toml
   [server]
   enableXsrfProtection = true
   enableCORS = false
   ```

3. **Access Control**
   - Implement authentication if needed
   - Use IP whitelisting where appropriate
   - Limit file upload sizes
   - Disable directory listing

4. **Monitoring**
   - Log all API calls
   - Monitor for unusual patterns
   - Set up alerts for errors
   - Track API quota usage

## Known Security Considerations

### Current Implementation

#### ✅ Implemented
- Input sanitization for XSS prevention
- Rate limiting (10 second cooldown)
- Secure API key management via secrets
- XSRF protection enabled
- No permanent data storage
- Error message sanitization

#### ⚠️ Considerations
- **Session State**: Stored in browser, cleared on page refresh
- **API Costs**: Monitoring responsibility on user
- **Input Limits**: 5000 characters max per field
- **No Authentication**: Application is publicly accessible
- **No User Data**: Nothing stored server-side

### Third-Party Services

#### Google Gemini API
- **Data Handling**: Requests sent to Google for processing
- **Privacy**: Review [Google's Privacy Policy](https://policies.google.com/privacy)
- **Data Retention**: Per Google's AI Terms of Service
- **Compliance**: User responsible for compliance with local laws

## Compliance

### GDPR Considerations

If deploying in EU or handling EU user data:

1. **Data Minimization**: Only collect necessary information
2. **User Rights**: Implement data export/deletion
3. **Consent**: Add cookie/privacy consent banner
4. **Privacy Policy**: Create comprehensive privacy policy
5. **Data Processing Agreement**: With Google for Gemini API

### CCPA Considerations

If handling California resident data:

1. **Privacy Notice**: Disclose data collection practices
2. **User Rights**: Implement "Do Not Sell" mechanism
3. **Opt-Out**: Allow users to opt-out of data sharing

## Security Checklist

### Before Deployment

- [ ] API keys stored securely in secrets/environment variables
- [ ] HTTPS configured with valid certificate
- [ ] XSRF protection enabled
- [ ] Input validation and sanitization implemented
- [ ] Rate limiting configured
- [ ] Error logging set up (without sensitive data)
- [ ] Dependencies updated to latest secure versions
- [ ] Security headers configured
- [ ] Privacy policy created (if applicable)
- [ ] Monitoring and alerting configured

### Regular Maintenance

- [ ] Update dependencies monthly
- [ ] Review security logs weekly
- [ ] Rotate API keys quarterly
- [ ] Test security measures monthly
- [ ] Review access logs for suspicious activity
- [ ] Check for new CVEs in dependencies
- [ ] Update security documentation

## Incident Response Plan

### If You Suspect a Breach

1. **Immediate Actions**
   - Disconnect affected systems
   - Rotate all API keys immediately
   - Document everything
   - Notify stakeholders

2. **Investigation**
   - Review logs for unauthorized access
   - Identify compromised data
   - Determine attack vector
   - Assess impact

3. **Remediation**
   - Apply security patches
   - Close security gaps
   - Update access controls
   - Implement additional monitoring

4. **Communication**
   - Notify affected users if applicable
   - Report to relevant authorities if required
   - Update security documentation
   - Share lessons learned

## Security Resources

### Tools

- **Dependency Scanning**: `pip-audit`, Snyk
- **Secret Scanning**: GitGuardian, TruffleHog
- **SAST**: Bandit, SonarQube
- **Vulnerability Database**: CVE, NVD

### Learning Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Streamlit Security Guide](https://docs.streamlit.io/library/advanced-features/security-and-secrets)

## Hall of Fame

Security researchers who have responsibly disclosed vulnerabilities:

- *No vulnerabilities reported yet*

Thank you to all security researchers who help keep this project secure!

## Contact

For security-related questions:
- **Security Issues**: Private email to maintainer
- **General Questions**: GitHub Discussions
- **Documentation**: GitHub Issues

---

**Last Updated**: February 2026

**Remember**: Security is everyone's responsibility. If you see something, say something! 🔒
