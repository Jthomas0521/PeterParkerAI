from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def crawl_website(url, use_selenium=False):
    try:
        if use_selenium:
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.get(url)
            html_content = driver.page_source
            driver.quit()
        else:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            html_content = response.text

        # Parse HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract data
        title = soup.title.string if soup.title else "No title found."
        headers = [header.get_text(strip=True) for header in soup.find_all(["h1", "h2", "h3"])]
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
        links = [a["href"] for a in soup.find_all("a", href=True)]

        # Convert to DataFrame
        data = {
            "title": [title],
            "headers": [headers],
            "paragraphs": [paragraphs[:5]],
            "links": [links[:5]],
        }

        return pd.DataFrame(data)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return pd.DataFrame()