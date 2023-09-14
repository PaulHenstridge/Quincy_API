import requests
from datetime import datetime

from .query_api import query_API
from .add_content_tags import add_content_tags
from ...db.update_db import update_quotes_collection
from ...models.email_link import EmailLink
from ...models.quote import Quote

# from .test_data import data

data_url = "https://raw.githubusercontent.com/sourabh-joshi/awesome-quincy-larson-emails/main/emails.json"

# allowing the date to be parsed in either abbreviated or full word format
def flexible_strptime(date_str):
    formats = ["%b %d, %Y", "%B %d, %Y"] 
    for format in formats:
        try:
            return datetime.strptime(date_str, format)
        except ValueError:
            pass
    raise ValueError(f"time data {date_str!r} does not match any of the provided formats")


def fetch_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def process_data(data): 
    quote_data = []
    link_data = []
   
    for email in data["emails"]:
        if not Quote.objects(date=email["date"]).first():
            quote_data.append(
                {
                    "date": email.get("date", None),
                    "date_time":flexible_strptime(email.get("date", "Jan 1 2000")),
                    "quote": email.get("quote", None),
                    "author": email.get("quote_author", None)
                }
            )

        for link in email["links"]:
            if link.get("link") and not EmailLink.objects(link=link["link"]).first():

                link_data.append(
                    {
                        "date": email.get("date", None),
                        "date_time":flexible_strptime(email.get("date", "Jan 1 2000")),
                        "tags":[],
                        "description": link.get("description", None),
                        "link": link.get("link", None),
                        "length": link.get("time_duration", ".") + link.get("time_type", "."),
                        "length_mins": float(link.get("time_duration", 0)) * (60 if link.get("time_type", None) == 'hours' else 1)  
                    }
                )
    return link_data, quote_data  

def get_data():
    data = fetch_data(data_url)  
    if data:
        link_data, quote_data = process_data(data)

    update_quotes_collection(quote_data)
    add_content_tags(link_data)
    
