---
title: Task Automation Agent
emoji: ✨
colorFrom: indigo
colorTo: blue
sdk: docker
app_port: 7860
---

# Task Automation Agent

A simple Streamlit interface powered by the Google Gemini API. Enter a topic and receive a concise three-point AI-generated brief.

## 1. Get a Gemini API key

Create a key in Google AI Studio: https://aistudio.google.com/app/apikey

## 2. Run locally on Windows PowerShell

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
streamlit run app.py
```

Open http://localhost:8501.

## 3. Test

```powershell
python -m unittest discover -s tests -v
```

## 4. Push to GitHub

Create an empty GitHub repository, then run these commands from this project folder. Replace the URL with your repository URL.

```bash
git init
git branch -M main
git add .
git commit -m "Add Gemini-powered task automation agent"
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```

The `.gitignore` file excludes local secrets. Never commit your API key.

## 5. Deploy on Hugging Face Spaces

1. Open https://huggingface.co/new-space.
2. Choose a Space name and select **Docker** as the SDK.
3. Create the Space.
4. Open Space **Settings → Variables and secrets**.
5. Add a secret named `GEMINI_API_KEY` and paste your Gemini API key as its value.
6. Connect the Space to GitHub by pushing the same project to the Space's Git remote, or deploy manually by adding the Space remote:

```bash
git remote add space https://huggingface.co/spaces/HF_USERNAME/SPACE_NAME
git push space main
```

Replace `HF_USERNAME` and `SPACE_NAME` with your actual values. If Git asks for credentials, use your Hugging Face username and a Hugging Face access token with write permission as the password.

7. Wait for the Docker build to finish. Open the Space page to get your public application link.

## 6. GitHub Actions

The included workflow runs unit tests, checks Python syntax, and builds the Docker image on pushes and pull requests to `main`. This provides CI evidence in the GitHub **Actions** tab. Deployment to Hugging Face can be done using the Space Git remote commands above.

## Notes

- The app uses Gemini, not the ChatGPT/OpenAI API. A Gemini API key is required for generating a brief.
- The app provides an AI-generated overview; it does not perform live web search or cite sources.
- API usage and quotas depend on your Google AI Studio account and selected model availability.
