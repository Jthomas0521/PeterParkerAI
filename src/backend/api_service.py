from fastapi import FastAPI
from dotenv import load_dotenv
from crawler import crawl_website
import json
import os

load_dotenv()

app = FastAPI()

@app.get("/crawl")
def crawl(url: str, selenium: bool = os.getenv("USE_SELENIUM", "False").lower() == "true"):
    result = crawl_website(url, use_selenium=selenium)
    return json.loads(result.to_json(orient="records"))
