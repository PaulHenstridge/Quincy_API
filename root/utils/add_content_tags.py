#from .get_data import get_data
from .scrape_content import scrape_content
from .query_api import query_API

# link_data, quote_data = get_data()

def add_content_tags(link_data):
    for link in link_data:
        article_text = scrape_content(link["link"])
        AI_response = query_API(article_text)
        print(AI_response)
        #link["tags"] = AI_response   think about how we want the data - list, string?
        # above adds it ass a string.  research ways of searching  in py
        #if ok, add the tags to the link_data dict