Deploy Canteen Billing (Flask) to the cloud (24/7)

This guide gives you an HTTPS URL that works even when your laptop is off. Two simple hosts are shown: Render and Railway. Both have free tiers.

1) Files already added

- requirements.txt
- Procfile

These are enough for most PaaS hosts.

2) Push this project to GitHub

```
# from project root
git init
git add .
git commit -m "Initial deploy"
# create a new repo on GitHub, then:
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

3) Deploy on Render (recommended)

1. Go to https://render.com → New → Web Service
2. Connect your GitHub repo
3. Settings:
   - Runtime: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --workers 2 --threads 4 --timeout 60`
   - Region: close to you
4. Create Web Service and wait for the deploy to finish.
5. You’ll get an `https://…render.com` URL. Open it in Chrome → the app is installable as a PWA.

4) Deploy on Railway (alternative)

1. Go to https://railway.app → New Project → Deploy from GitHub Repo
2. It auto-detects Python.
3. Add variables if prompted (none needed here).
4. Start command: `gunicorn app:app --workers 2 --threads 4 --timeout 60`
5. After deploy, open the generated HTTPS URL.

5) Local production run (optional)

```
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

Troubleshooting

- If build fails: ensure `requirements.txt` exists and is in project root.
- If app boots but returns error: check logs on the host. Flask debug isn’t needed in the cloud; Gunicorn runs it in production mode.
- PWA install not showing: the cloud URL must be HTTPS (Render/Railway provide it). Clear site data and reload if needed.

After deployment, share the HTTPS link with users. They can tap “Install app” in Chrome to add it to their home screen.

