# AutoCare Services - Render Deployment Guide

## ✅ Prerequisites Completed

1. ✅ `requirements.txt` updated with gunicorn and whitenoise
2. ✅ `build.sh` script created for deployment
3. ✅ `settings.py` configured for production
4. ✅ `render.yaml` configuration file created
5. ✅ `.gitignore` updated

---

## 📋 Deployment Steps

### Step 1: Push Changes to GitHub

```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin master
```

### Step 2: Create Render Account

1. Go to [https://render.com](https://render.com)
2. Sign up with your GitHub account
3. Authorize Render to access your repositories

### Step 3: Create New Web Service

1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `CodeXplorer712/AutoCare`
3. Configure the following:

**Basic Settings:**
- **Name**: `autocare-services` (or your preferred name)
- **Runtime**: `Python 3`
- **Branch**: `master`
- **Root Directory**: (leave blank)

**Build & Deploy:**
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn autocare_project.wsgi:application`

### Step 4: Set Environment Variables

Add these environment variables in Render dashboard:

| Key | Value | Notes |
|-----|-------|-------|
| `PYTHON_VERSION` | `3.11.0` | Python version |
| `SECRET_KEY` | `(auto-generate)` | Click "Generate" button |
| `DEBUG` | `False` | Production mode |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` | Your Render URL |

**Important:** Replace `your-app-name` with your actual Render app name!

### Step 5: Deploy!

1. Click "Create Web Service"
2. Render will automatically:
   - Clone your repository
   - Run `build.sh` script
   - Install dependencies
   - Collect static files
   - Run migrations
   - Start gunicorn server

### Step 6: Access Your App

Once deployment is complete (5-10 minutes):
- Your app will be available at: `https://your-app-name.onrender.com`

---

## 🔧 Post-Deployment

### Create Superuser (Admin Account)

1. In Render dashboard → Shell tab
2. Run: `python manage.py createsuperuser`
3. Follow prompts to create admin account
4. Access admin at: `https://your-app-name.onrender.com/admin/`

### Monitor Logs

- Click "Logs" tab in Render dashboard
- Monitor for any errors or issues

---

## ⚠️ Important Notes

### Free Tier Limitations

- Service spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- Database resets when service restarts (SQLite limitation)

### Production Recommendations

For production use:
1. **Upgrade to paid plan** for always-on service
2. **Add PostgreSQL database** (Render offers free PostgreSQL)
3. **Set up custom domain**
4. **Enable automatic deploys** from GitHub

---

## 🐛 Troubleshooting

### Static Files Not Loading

- Check `STATIC_ROOT` in settings.py
- Verify `collectstatic` ran in build logs
- Ensure `WhiteNoiseMiddleware` is in MIDDLEWARE

### Database Issues

- SQLite resets on each deploy
- For persistent data, switch to PostgreSQL:
  ```python
  # In settings.py
  import dj_database_url
  DATABASES = {
      'default': dj_database_url.config(default='sqlite:///db.sqlite3')
  }
  ```

### Application Errors

- Check Render logs for errors
- Verify environment variables are set correctly
- Ensure `DEBUG=False` in production

---

## 📚 Additional Resources

- [Render Django Documentation](https://render.com/docs/deploy-django)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

---

**Your AutoCare Services app is ready to deploy to Render!** 🚀
