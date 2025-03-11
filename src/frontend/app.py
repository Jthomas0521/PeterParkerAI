import streamlit as st
import pandas as pd
import requests
# import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "http://backend:8000/crawl"

st.title("Peter Parker AI")

url = st.text_input("Enter a website URL to crawl:")
use_selenium = st.checkbox("Use Selenium (Javascript-heavy websites.)")

if st.button("Crawl"):
    if url:
        with st.spinner("Crawling..."):
            response = requests.post(API_URL, json={"url": url, "use_selenium": use_selenium})
            if response.status_code == 200:
                result = pd.DataFrame(response.json())
                st.dataframe(result)
                st.download_button("Download CSV", result.to_csv(index=False), "crawled_data.csv", "text/csv")
            else:
                st.error("An error occurred while crawling the website.")
    else:
        st.warning("Please enter a valid URL to crawl.")
