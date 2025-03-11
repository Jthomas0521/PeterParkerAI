FROM python:3.12-bookworm AS build

WORKDIR /app

# Install dependencies
COPY requirements.backend.txt .
RUN pip install --no-cache-dir -r requirements.backend.txt

# Install Chromedriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Copy source code
COPY . .

# Expose API port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "api_service:app", "--host", "0.0.0.0", "--port", "8000"]
