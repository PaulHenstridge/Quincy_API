import requests
from datetime import datetime

from .query_api import query_API
from .add_content_tags import add_content_tags
from .filter_unprocessed import filter_unprocessed_links, filter_unprocessed_quotes
from ...db.update_db import update_quotes_collection


#this func allows the date to be parsed in either abbreviated or full word format
# TODO - extract to helpers/utils folder
def flexible_strptime(date_str):
    formats = ["%b %d, %Y", "%B %d, %Y"] 
    for format in formats:
        try:
            return datetime.strptime(date_str, format)
        except ValueError:
            pass
    raise ValueError(f"time data {date_str!r} does not match any of the provided formats")



def get_data():
    response = requests.get(
        "https://raw.githubusercontent.com/sourabh-joshi/awesome-quincy-larson-emails/main/emails.json"
    )

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")



    quote_data = []
    link_data = []
   
    # - TODO should probably filter at this point - if not in DB already then add to data.  consider refactor
    for email in data["emails"]:
        quote_data.append({
        "date": email.get("date", None),
        "date_time":flexible_strptime(email.get("date", "Jan 1 2000")),
        "quote": email.get("quote", None),
        "author": email.get("quote_author", None)
    })
        for link in email["links"]:
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
    
    unprocessed_quotes = filter_unprocessed_quotes(quote_data)
    unprocessed_links = filter_unprocessed_links(link_data)

    update_quotes_collection(unprocessed_quotes)
    add_content_tags(unprocessed_links)
    
