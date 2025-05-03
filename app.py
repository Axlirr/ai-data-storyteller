import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from gtts import gTTS
import tempfile
import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

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
    numeric_cols = data.select_dtypes(include=np.number).columns.tolist()
    if numeric_cols:
        col1, col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox("X-axis", numeric_cols, key="x")
        with col2:
            y_axis = st.selectbox("Y-axis", numeric_cols, key="y")
        if x_axis and y_axis:
            fig = px.scatter(data, x=x_axis, y=y_axis, title=f"Scatter: {x_axis} vs {y_axis}")
            st.plotly_chart(fig)
    else:
        st.info("No numeric columns for plotting.")

    # --- AI Insights (Gemini) ---
    st.subheader("AI-Generated Insights")

    if st.button("Generate Insights with Gemini"):
        if not GEMINI_API_KEY:
            st.error("Gemini API key is missing. Please check your .env file.")
        else:
            prompt = f"""
            You are an expert data analyst. Analyze the following dataset summary and statistics, and provide key insights, trends, and possible recommendations in plain English.

            Summary:
            {data.describe(include='all').to_string()}

            Missing Values:
            {data.isnull().sum().to_string()}
            """
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GEMINI_API_KEY}"
            }
            payload = {"contents": [{"parts": [{"text": prompt}]}]}
            response = requests.post(
                "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
                headers=headers,
                json=payload
            )

            if response.status_code == 200:
                gemini_text = response.json()['candidates'][0]['content']['parts'][0]['text']
                st.success("✅ AI Insights generated successfully!")
                st.markdown(gemini_text)
            else:
                st.error(f"Gemini API error ({response.status_code}): {response.text}")

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

