import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from gtts import gTTS
import tempfile
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# --- Streamlit UI Setup ---
st.set_page_config(page_title="AI Data Storyteller", layout="wide")
st.title("AI Data Storyteller")

st.markdown("""
Upload a CSV or provide a dataset URL. The app will analyze your data, generate insights using Gemini LLM, create visualizations, and narrate a report!
""")

# --- Data Upload ---
data = None
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
dataset_url = st.text_input("Or enter a public CSV URL:")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
elif dataset_url:
    try:
        data = pd.read_csv(dataset_url)
    except Exception as e:
        st.error(f"Failed to load data from URL: {e}")

# --- If data is loaded ---
if data is not None:
    st.subheader("Data Preview")
    st.dataframe(data.head())

    # --- Basic EDA ---
    st.subheader("Summary Statistics")
    st.write(data.describe(include='all'))

    st.subheader("Missing Values")
    st.write(data.isnull().sum())

    # --- Visualizations ---
    st.subheader("Visualizations")
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        st.subheader("Correlation Heatmap")
        corr_matrix = data[numeric_cols].corr()
        fig = px.imshow(corr_matrix, text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

    # --- AI Insights ---
    def get_gemini_insights(data):
        try:
            # Load credentials
            credentials = service_account.Credentials.from_service_account_file(
                os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
            )
            
            # Refresh token if needed
            if not credentials.valid:
                credentials.refresh(Request())
            
            # Get access token
            access_token = credentials.token
            
            # Prepare the data for Gemini
            data_summary = "\n".join([
                f"{col}: {data[col].describe().to_string()}" for col in data.columns
            ])
            
            # Generate insights using Gemini
            url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }
            
            prompt = f"""
            Analyze this dataset and provide insights:
            {data_summary}
            
            Please provide:
            1. Key patterns and trends
            2. Any correlations between variables
            3. Potential areas for further investigation
            4. Any anomalies or outliers
            """
            
            payload = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                if "candidates" in result and len(result["candidates"]) > 0:
                    insights = result["candidates"][0]["content"]["parts"][0]["text"]
                    st.success("AI Insights:")
                    st.write(insights)
            else:
                try:
                    error_msg = response.json().get("error", {}).get("message", "Unknown error")
                    st.error(f"Gemini API error ({response.status_code}): {error_msg}")
                except:
                    st.error(f"Gemini API error ({response.status_code}): {response.text}")
        except Exception as e:
            st.error(f"Failed to authenticate with Gemini API: {str(e)}")

    if st.button("Generate Insights with Gemini"):
        get_gemini_insights(data)

    # --- Narrate Report ---
    st.subheader("Narrate Report (TTS)")
    report_text = st.text_area("Paste or edit the report to narrate:")
    if st.button("Generate Audio") and report_text:
        tts = gTTS(text=report_text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")

    # --- Export PDF ---
    st.subheader("Export Report as PDF")
    pdf_text = st.text_area("Paste or edit the report for PDF export:")
    if st.button("Download PDF") and pdf_text:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as fp:
            c = canvas.Canvas(fp.name, pagesize=letter)
            width, height = letter
            lines = pdf_text.split('\n')
            y = height - 40
            for line in lines:
                c.drawString(40, y, line)
                y -= 15
                if y < 40:
                    c.showPage()
                    y = height - 40
            c.save()
            with open(fp.name, "rb") as pdf_file:
                st.download_button("Download PDF", pdf_file, file_name="report.pdf")
else:
    st.info("Please upload a CSV or provide a dataset URL to get started.")