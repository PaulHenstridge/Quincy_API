import requests
from bs4 import BeautifulSoup
from .query_api import query_API

def scrape_content(link):
    response = requests.get(link)
    #scrape the text content of the article
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all("article")
    article_text = ''.join(article.text for article in articles)
    return article_text


# res = scrape_content('https://www.freecodecamp.org/news/explaining-the-best-javascript-meme-i-have-ever-seen/')
# print(res)
# APIres = query_API(res)
# print(APIres)