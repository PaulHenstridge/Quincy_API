import requests
from datetime import datetime

#this func allows the date to be parsed in either abbreviated or full word format
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

    quotes_data = []
    db_data = []
   

    for email in data["emails"]:
        quotes_data.append({
        "date": email.get("date", None),
        "quote": email.get("quote", None),
        "author": email.get("quote_author", None)
    })
        for link in email["links"]:
            db_data.append(
                {
                    "date": email.get("date", None),
                    "date_time":flexible_strptime(email.get("date", "Jan 1 2000")),
                    "quote": [email.get("quote", None), email.get("quote_author")],
                    "description": link.get("description", None),
                    "link": link.get("link", None),
                    "length": link.get("time_duration", ".") + link.get("time_type", "."),
                    "length_mins": float(link.get("time_duration", 0)) * (60 if link.get("time_type", None) == 'hours' else 1)  
                }
            )
    return db_data, quotes_data
