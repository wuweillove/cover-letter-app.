# 🚀 Deployment Guide

Complete guide for deploying Cover Letter Pro to various platforms.

## Table of Contents
- [Streamlit Cloud](#streamlit-cloud-recommended)
- [Heroku](#heroku)
- [Docker](#docker)
- [AWS](#aws)
- [Google Cloud Platform](#google-cloud-platform)
- [Azure](#azure)
- [Self-Hosted](#self-hosted)

---

## Streamlit Cloud (Recommended)

**Pros:** Free tier available, easy setup, automatic deployments
**Cons:** Limited resources on free tier

### Prerequisites
- GitHub account
- Google Gemini API key
- Streamlit Cloud account

### Step-by-Step Deployment

1. **Fork the Repository**
   - Go to https://github.com/wuweillove/cover-letter-app.
   - Click "Fork" in the top right
   - Wait for the fork to complete

2. **Sign Up for Streamlit Cloud**
   - Visit https://streamlit.io/cloud
   - Sign in with your GitHub account
   - Authorize Streamlit to access your repositories

3. **Create New App**
   - Click "New app"
   - Select your forked repository
   - Set main file path: `app.py`
   - Choose a custom URL (optional)

4. **Configure Secrets**
   - Click "Advanced settings"
   - Add to secrets:
     ```toml
     GOOGLE_API_KEY = "your-google-gemini-api-key-here"
     ```

5. **Deploy**
   - Click "Deploy!"
   - Wait 2-3 minutes for deployment
   - Your app will be live at: `https://your-app-name.streamlit.app`

### Updating Your Deployment

Streamlit Cloud automatically redeploys when you push to the connected branch:
```bash
git add .
git commit -m "Update application"
git push origin main
```

### Troubleshooting Streamlit Cloud

**Issue: App won't start**
- Check logs in Streamlit Cloud dashboard
- Verify secrets are configured correctly
- Ensure requirements.txt is valid

**Issue: API errors**
- Verify API key in secrets
- Check API quota in Google Cloud Console

---

## Heroku

**Pros:** Reliable, scalable, good free tier
**Cons:** Requires more configuration

### Prerequisites
- Heroku account
- Heroku CLI installed
- Git

### Deployment Steps

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Windows
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   
   # Linux
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-cover-letter-app
   ```

4. **Create Required Files**

   **Procfile:**
   ```
   web: sh setup.sh && streamlit run app.py
   ```

   **setup.sh:**
   ```bash
   mkdir -p ~/.streamlit/
   
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   ```

   **runtime.txt:**
   ```
   python-3.9.16
   ```

5. **Set Environment Variables**
   ```bash
   heroku config:set GOOGLE_API_KEY=your-api-key-here
   ```

6. **Deploy**
   ```bash
   git add .
   git commit -m "Prepare for Heroku deployment"
   git push heroku main
   ```

7. **Open Your App**
   ```bash
   heroku open
   ```

### Updating Heroku Deployment

```bash
git add .
git commit -m "Update application"
git push heroku main
```

### Heroku Monitoring

```bash
# View logs
heroku logs --tail

# Check app status
heroku ps

# Restart app
heroku restart
```

---

## Docker

**Pros:** Consistent environment, portable, works anywhere
**Cons:** Requires Docker knowledge

### Dockerfile

Create `Dockerfile` in project root:

```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create .streamlit directory
RUN mkdir -p ~/.streamlit/

# Configure Streamlit
RUN echo "\
[server]\n\
headless = true\n\
port = 8501\n\
enableCORS = false\n\
\n\
[browser]\n\
gatherUsageStats = false\n\
" > ~/.streamlit/config.toml

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run application
CMD ["streamlit", "run", "app.py"]
```

### Docker Compose (Optional)

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
    restart: unless-stopped
    volumes:
      - ./:/app
```

### Building and Running

```bash
# Build image
docker build -t cover-letter-app .

# Run container
docker run -p 8501:8501 \
  -e GOOGLE_API_KEY=your-api-key \
  cover-letter-app

# Or with docker-compose
docker-compose up -d
```

### Docker Hub Deployment

```bash
# Tag image
docker tag cover-letter-app your-username/cover-letter-app:latest

# Push to Docker Hub
docker push your-username/cover-letter-app:latest

# Pull and run anywhere
docker pull your-username/cover-letter-app:latest
docker run -p 8501:8501 -e GOOGLE_API_KEY=key your-username/cover-letter-app
```

---

## AWS

**Pros:** Highly scalable, many services, reliable
**Cons:** More complex, potential costs

### AWS Elastic Beanstalk

1. **Install AWS CLI and EB CLI**
   ```bash
   pip install awscli awsebcli
   ```

2. **Initialize EB**
   ```bash
   eb init -p python-3.9 cover-letter-app
   ```

3. **Create Environment**
   ```bash
   eb create cover-letter-env
   ```

4. **Set Environment Variables**
   ```bash
   eb setenv GOOGLE_API_KEY=your-api-key
   ```

5. **Deploy**
   ```bash
   eb deploy
   ```

6. **Open App**
   ```bash
   eb open
   ```

### AWS ECS (Docker)

1. **Push to ECR**
   ```bash
   aws ecr create-repository --repository-name cover-letter-app
   docker tag cover-letter-app:latest xxx.ecr.region.amazonaws.com/cover-letter-app
   docker push xxx.ecr.region.amazonaws.com/cover-letter-app
   ```

2. **Create ECS Task Definition**
3. **Create ECS Service**
4. **Configure Load Balancer**

---

## Google Cloud Platform

### Cloud Run (Recommended for GCP)

1. **Install gcloud CLI**

2. **Authenticate**
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

3. **Deploy**
   ```bash
   gcloud run deploy cover-letter-app \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars GOOGLE_API_KEY=your-api-key
   ```

### App Engine

1. **Create app.yaml**
   ```yaml
   runtime: python39
   entrypoint: streamlit run app.py --server.port $PORT
   
   env_variables:
     GOOGLE_API_KEY: "your-api-key"
   ```

2. **Deploy**
   ```bash
   gcloud app deploy
   ```

---

## Azure

### Azure App Service

1. **Install Azure CLI**

2. **Create Resource Group**
   ```bash
   az group create --name CoverLetterAppRG --location eastus
   ```

3. **Create App Service Plan**
   ```bash
   az appservice plan create \
     --name CoverLetterPlan \
     --resource-group CoverLetterAppRG \
     --sku B1 \
     --is-linux
   ```

4. **Create Web App**
   ```bash
   az webapp create \
     --resource-group CoverLetterAppRG \
     --plan CoverLetterPlan \
     --name your-cover-letter-app \
     --runtime "PYTHON|3.9"
   ```

5. **Configure Settings**
   ```bash
   az webapp config appsettings set \
     --resource-group CoverLetterAppRG \
     --name your-cover-letter-app \
     --settings GOOGLE_API_KEY=your-api-key
   ```

6. **Deploy**
   ```bash
   az webapp up --name your-cover-letter-app
   ```

---

## Self-Hosted

### Ubuntu Server Setup

1. **Update System**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Python and Dependencies**
   ```bash
   sudo apt install python3.9 python3-pip nginx -y
   ```

3. **Clone Repository**
   ```bash
   git clone https://github.com/wuweillove/cover-letter-app..git
   cd cover-letter-app.
   ```

4. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Configure Secrets**
   ```bash
   mkdir -p .streamlit
   echo 'GOOGLE_API_KEY = "your-key"' > .streamlit/secrets.toml
   ```

6. **Create Systemd Service**
   ```bash
   sudo nano /etc/systemd/system/coverletterapp.service
   ```

   ```ini
   [Unit]
   Description=Cover Letter Pro
   After=network.target

   [Service]
   User=your-user
   WorkingDirectory=/path/to/cover-letter-app.
   ExecStart=/path/to/venv/bin/streamlit run app.py --server.port 8501
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

7. **Start Service**
   ```bash
   sudo systemctl enable coverletterapp
   sudo systemctl start coverletterapp
   ```

8. **Configure Nginx**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:8501;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
       }
   }
   ```

9. **Enable SSL (Optional)**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d your-domain.com
   ```

---

## Environment Variables

All deployment methods require these environment variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_API_KEY` | Yes | Google Gemini API key |
| `PORT` | No | Port to run on (default: 8501) |

---

## Post-Deployment Checklist

- [ ] Application loads without errors
- [ ] API key is working correctly
- [ ] All features function properly
- [ ] SSL certificate is configured (production)
- [ ] Monitoring is set up
- [ ] Backups configured (if applicable)
- [ ] Domain is connected (if applicable)
- [ ] Error logging is working
- [ ] Performance is acceptable
- [ ] Security headers are set

---

## Monitoring and Maintenance

### Health Checks
- Set up uptime monitoring (UptimeRobot, Pingdom)
- Configure error logging
- Monitor API usage and costs

### Regular Maintenance
- Update dependencies monthly
- Review logs weekly
- Monitor API quotas
- Check for security updates

---

## Cost Estimates

| Platform | Free Tier | Estimated Monthly Cost |
|----------|-----------|----------------------|
| Streamlit Cloud | Yes | $0 - $20 |
| Heroku | Yes (limited) | $0 - $7 |
| AWS | 12 months | $5 - $50 |
| GCP | $300 credit | $5 - $30 |
| Azure | $200 credit | $5 - $40 |
| Self-Hosted | N/A | $5 - $20 (VPS) |

---

## Support

For deployment issues:
- Check platform-specific documentation
- Review application logs
- Open an issue on GitHub
- Join our Discord community

---

**Happy Deploying! 🚀**
