![placeholder](https://github.com/DanielBash/profile/blob/main/.github/github-banner.png?raw=true)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Stars](https://img.shields.io/github/stars/DanielBash/profile)

# Profile Website

> This is source code of DanielBash's profile website

This masterpiece is hosted [here](https://hell-0.ru)!

## Local setup (idk why you would try to do this though)
### Option 1: Python virtual environment
1) Download repository
```bash
git clone https://github.com/DanielBash/profile.git
cd profile
```

2) Install required packages
```bash
pip install -r requirements.txt
```

3) Modify .env if needed. All available settings can be found in settings_templates.default module.
```bash
echo "SECRET_KEY=secure-secret-key" > .env
```

4) Run script <br/>

**Option 1.1**: Run script for debug
```bash
python main.py
```

**Option 1.2**: Run production script
```bash
gunicorn --config gunicorn_config.py main:app
```

### Option 2: Docker-container
1) Pull relevant container from docker hub:
```bash
docker pull danielbashl/profile:latest
```

2) Launch container:
```bash
docker run -d -p 8000:5000 danielbashl/profile:latest
```
