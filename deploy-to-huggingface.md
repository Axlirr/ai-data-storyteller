# Deploying AI Data Storyteller to Hugging Face Spaces

Hugging Face Spaces is a great way to host Streamlit apps for free. Here’s how to deploy your project:

## 1. Prepare Your Repo
- Ensure your repo contains:
  - `app.py` (Streamlit app)
  - `requirements.txt`
  - `.env.example` (for API key)

## 2. Add a `README.md` badge (optional)
You can add a badge to your README after deployment.

## 3. Create a New Space
- Go to [Hugging Face Spaces](https://huggingface.co/spaces)
- Click **Create new Space**
- Name your space (e.g., `axlirr/ai-data-storyteller`)
- Choose **Streamlit** as the SDK
- Connect your GitHub repo or upload files manually

## 4. Set Environment Variables
- In the Space settings, add your `GEMINI_API_KEY` as a secret environment variable.

## 5. Deploy
- The app will build and deploy automatically.
- If you update your repo, the Space will redeploy.

## 6. Share
- Share your Hugging Face Space link in your portfolio!

---

**Tip:** For other cloud options, see the Docker instructions in the main README.
