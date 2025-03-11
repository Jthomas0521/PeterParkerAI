from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from crawler import crawl_website
import os
import logging

load_dotenv()

app = FastAPI()


class CrawlRequest(BaseModel):
    url: str
    use_selenium: bool = os.getenv("USE_SELENIUM", "False").lower() == "true"


@app.post("/crawl")
def crawl(request: CrawlRequest):
    try:
        result = crawl_website(request.url, use_selenium=request.use_selenium)
        return result.to_dict(orient="records")
    except Exception as e:
        logging.error(f"An error occurred while crawling the website: {e}")
        raise HTTPException(status_code=500, detail=str(e))
