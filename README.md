# PeterParkerAI

PeterParkerAI is a web scraping application built with FastAPI and Streamlit. It uses Selenium and Chromedriver to scrape websites and provides an API to interact with the scraper.

## Features

- FastAPI backend for handling web scraping requests
- Streamlit frontend for user interaction
- Selenium and Chromedriver for web scraping
- Dockerized for easy deployment

## Prerequisites

- Docker
- Docker Compose

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/PeterParkerAI.git
    cd PeterParkerAI
    ```

2. Create a [.env](http://_vscodecontentref_/1) file in the root directory with the following content:

    ```properties
    STREAMLIT_PORT=8501
    STREAMLIT_SERVER_HEADLESS=True
    FASTAPI_PORT=8000
    USE_SELENIUM=True
    ```

3. Build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

## Usage

1. Access the Streamlit frontend at [http://localhost:8501](http://localhost:8501).

2. Use the FastAPI backend to send web scraping requests:

    ```bash
    curl -X POST "http://localhost:8000/crawl" -H "Content-Type: application/json" -d '{"url": "https://example.com", "use_selenium": true}'
    ```

## Project Structure

```plaintext
PeterParkerAI/
├── .env
├── docker-compose.yml
├── requirements.txt
├── src/
│   ├── backend/
│   │   ├── api_service.py
│   │   ├── Dockerfile
│   │   ├── requirements.backend.txt
│   │   └── ...
│   └── frontend/
│       ├── app.py
│       ├── Dockerfile
│       ├── requirements.frontend.txt
│       └── ...
└── README.md