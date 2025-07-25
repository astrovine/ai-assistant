# 🚀 Deployment Guide for Dhee AI Assistant

## Quick Deploy Options

### 1. 🟢 **Render (Recommended - Free)**
1. Go to [render.com](https://render.com)
2. Connect your GitHub account
3. Select "New Web Service"
4. Connect repository: `astrovine/ai-assistant`
5. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd src && gunicorn --bind 0.0.0.0:$PORT web_app:app`
   - **Environment Variables**:
     - `GROQ_API_KEY`: Your Groq API key
     - `FLASK_ENV`: production

### 2. 🟣 **Heroku (Popular)**
```bash
# Install Heroku CLI first
heroku create your-ai-assistant-name
heroku config:set GROQ_API_KEY=your_groq_api_key_here
heroku config:set FLASK_ENV=production
git push heroku main
```

### 3. 🔵 **Railway**
1. Go to [railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add environment variables:
   - `GROQ_API_KEY`: Your Groq API key
   - `FLASK_ENV`: production

### 4. 🟠 **Vercel**
```bash
# Install Vercel CLI
npm i -g vercel
vercel
# Follow prompts and add GROQ_API_KEY in dashboard
```

### 5. ⚫ **Local Production Test**
```bash
# Test production setup locally
export FLASK_ENV=production
export GROQ_API_KEY=your_key_here
pip install gunicorn
cd src && gunicorn --bind 0.0.0.0:5000 web_app:app
```

## 🔧 Environment Variables Needed

For any deployment platform, you need:
- `GROQ_API_KEY`: Your Groq API key from console.groq.com
- `FLASK_ENV`: Set to "production" for live deployment

## 🌐 Post-Deployment

After deployment, your AI assistant will be available at:
- **Render**: `https://your-service-name.onrender.com`
- **Heroku**: `https://your-app-name.herokuapp.com`
- **Railway**: `https://your-app-name.up.railway.app`
- **Vercel**: `https://your-project.vercel.app`

## 🛠 Troubleshooting

**Common Issues:**
1. **Build Fails**: Check Python version in runtime.txt
2. **App Crashes**: Verify GROQ_API_KEY is set correctly
3. **Slow Cold Starts**: Normal for free tiers

**Logs:**
- **Render**: View in dashboard
- **Heroku**: `heroku logs --tail`
- **Railway**: Check deployment logs in dashboard

## 🚀 Quick Start Commands

```bash
# 1. Commit your changes
git add .
git commit -m "deployment ready"
git push origin main

# 2. Choose a platform above and follow steps
# 3. Set environment variables
# 4. Deploy!
```

Your AI assistant will be live on the web! 🎉
