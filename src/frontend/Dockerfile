FROM python:3.12-bookworm AS build

WORKDIR /app

# Install dependencies
COPY requirements.frontend.txt .
RUN pip install --no-cache-dir -r requirements.frontend.txt

# Copy Streamlit app
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
