import requests
from bs4 import BeautifulSoup
from .query_api import query_API

def scrape_content(link):
    if not link:
        return None
    
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find(class_='post-full-content')
    if content:
        return content.text
    return None

