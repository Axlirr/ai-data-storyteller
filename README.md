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
1. Clone the repository:
   ```bash
   git clone https://github.com/Axlirr/ai-data-storyteller.git
   cd ai-data-storyteller
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Google Cloud credentials:
   1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
   2. Create a new project or select an existing one
   3. Enable the Generative AI API
   4. Create credentials (OAuth 2.0 Client IDs)
   5. Download the credentials JSON file
   6. Place the JSON file in your project directory
   7. Set the environment variable:
      ```bash
      export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
      ```

4. Run the application:
   ```bash
   python -m streamlit run app.py
   ```

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t ai-data-storyteller .
   ```
2. Run the container (pass your credentials file path):
   ```bash
   docker run -p 8501:8501 -e GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials.json ai-data-storyteller
   ```

## License
MIT