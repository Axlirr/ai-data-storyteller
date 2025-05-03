FROM python:3.9-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 8501 (default Streamlit port)
EXPOSE 8501

# Run Streamlit app
CMD ["python", "-m", "streamlit", "run", "app.py"]