# AI Data Storyteller

A powerful data analysis web app that analyzes datasets, generates insights, creates visualizations, and narrates reports with TTS. Built for Applied AI & Analytics portfolios.

## Features
- Upload CSV or import dataset from URL
- Automated data analysis (summary stats, missing values, correlations)
- Visualizations (interactive plots)
- Statistical insights using TextBlob
- Narrated report with Google Text-to-Speech (gTTS)
- Export report as PDF and audio as MP3

## Tech Stack
- Python (Streamlit, Pandas, NumPy, Plotly)
- TextBlob for text processing
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

3. Run the application:
   ```bash
   python -m streamlet run app.py
   ```

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t ai-data-storyteller .
   ```
2. Run the container:
   ```bash
   docker run -p 8501:8501 ai-data-storyteller
   ```

## License
MIT