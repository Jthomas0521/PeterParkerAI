FROM python:3.12-bookworm as build

WORKDIR /app

# Install dependencies
COPY requirements.backend.txt .
RUN pip install --no-cache-dir -r requirements.backend.txt

# Copy source code
COPY . .

# Expose API port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
