# AI Data Storyteller

A unique AI-powered web app that analyzes datasets, generates insights using Gemini LLM, creates visualizations, and narrates reports with TTS. Built for Applied AI & Analytics portfolios.

## Features
- Upload CSV or import dataset from URL
- Automated data analysis (summary stats, missing values, correlations)
- Visualizations (interactive plots)
- AI-generated insights using Gemini LLM
- Narrated report with Google Text-to-Speech (gTTS)
- Export report as PDF and audio as MP3

## Tech Stack
- Python (Streamlit, Pandas, NumPy, Plotly)
- Gemini LLM API
- gTTS (Google Text-to-Speech)

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/Axlirr/ai-data-storyteller.git
   cd ai-data-storyteller
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Gemini API key as an environment variable:
   ```bash
   export GEMINI_API_KEY="AIzaSyBVHvqRT38MdYzAn6YFWSQRFtC_gYFe79s"
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t ai-data-storyteller .
   ```
2. Run the container (pass your Gemini API key):
   ```bash
   docker run -p 8501:8501 -e GEMINI_API_KEY=your_gemini_api_key ai-data-storyteller
   ```

## License
MIT
