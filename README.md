# AI Data Storyteller

A unique AI-powered web app that analyzes datasets, generates insights using OpenAI's GPT-3.5 Turbo, creates visualizations, and narrates reports with TTS. Built for Applied AI & Analytics portfolios.

## Features
- Upload CSV or import dataset from URL
- Automated data analysis (summary stats, missing values, correlations)
- Visualizations (interactive plots)
- AI-generated insights using OpenAI's GPT-3.5 Turbo
- Narrated report with Google Text-to-Speech (gTTS)
- Export report as PDF and audio as MP3

## Tech Stack
- Python (Streamlit, Pandas, NumPy, Plotly)
- OpenAI's GPT-3.5 Turbo API
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

3. Set up OpenAI API key:
   1. Sign up for a free OpenAI account at https://platform.openai.com/signup
   2. Get your API key from https://platform.openai.com/api-keys
   3. Set the environment variable:
      ```bash
      set OPENAI_API_KEY="your_openai_api_key"
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
2. Run the container (pass your OpenAI API key):
   ```bash
   docker run -p 8501:8501 -e OPENAI_API_KEY=your_openai_api_key ai-data-storyteller
   ```

## License
MIT