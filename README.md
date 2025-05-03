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

3. Set up Google Cloud credentials:
   - Go to https://console.cloud.google.com/
   - Create a new project or select an existing one
   - Enable the Generative AI API
   - Create credentials (OAuth 2.0 Client IDs)
   - Download the credentials JSON file
   - Place the JSON file in your project directory
   - Rename the `.env.example` file to `.env`
   - Set the path to your credentials file in the `.env` file:
     ```
     SERVICE_ACCOUNT_FILE="path/to/your/service-account-file.json"
     ```

4. Run the app:
   ```bash
   python -m streamlit run app.py
   ```

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t ai-data-storyteller .
   ```
2. Run the container (pass your service account file path):
   ```bash
   docker run -p 8501:8501 -e SERVICE_ACCOUNT_FILE=/path/to/your/service-account-file.json ai-data-storyteller
   ```

## License
MIT