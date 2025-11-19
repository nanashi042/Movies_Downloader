# Deployment Guide for Render

## Prerequisites
- A Render account
- Your project pushed to a Git repository (GitHub, GitLab, or Bitbucket)

## Deployment Steps

### 1. Create a New Web Service on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" and select "Web Service"
3. Connect your repository

### 2. Configure Build Settings

**Build Command:**
pip install -r requirements.txt && python manage.py collectstatic --noinput**Start Command:**
gunicorn Moviesnation_scrape.wsgi:application### 3. Set Environment Variables

In the Render dashboard, add these environment variables:

- `SECRET_KEY`: Generate a new Django secret key (you can use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Set to your Render domain (e.g., `your-app.onrender.com`)
- `RAPIDAPI_KEY`: Your RapidAPI key
- `RAPIDAPI_HOST`: `imdb236.p.rapidapi.com`
- `PYTHON_VERSION`: `3.11.0` (or your preferred version)

### 4. Deploy

Render will automatically:
1. Build your application
2. Run migrations (if you add them to build command)
3. Start your web service

### 5. Access Your Application

Your app will be available at: `https://your-app-name.onrender.com`

## Alternative: Using render.yaml

If you use the `render.yaml` file:
1. Push it to your repository
2. In Render dashboard, select "Apply render.yaml" when creating the service
3. Render will automatically configure everything

## Troubleshooting

### Static Files Not Loading
- Ensure `whitenoise` is in `requirements.txt`
- Check that `collectstatic` runs in build command
- Verify `STATIC_ROOT` is set in settings.py

### Application Crashes
- Check logs in Render dashboard
- Verify all environment variables are set
- Ensure `ALLOWED_HOSTS` includes your Render domain

### Database Issues
- SQLite works for small apps, but consider PostgreSQL for production
- Add `python manage.py migrate` to build command if using migrations
