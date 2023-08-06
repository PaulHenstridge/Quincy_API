import requests


def get_data():
    response = requests.get(
        "https://raw.githubusercontent.com/sourabh-joshi/awesome-quincy-larson-emails/main/emails.json"
    )

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")

    db_data = []
    for email in data["emails"]:
        for link in email["links"]:
            db_data.append(
                {
                    "date": email.get("date", None),
                    "quote": [email.get("quote", None), email.get("quote_author")],
                    "description": link.get("description", None),
                    "link": link.get("link", None),
                    "length": [
                        link.get("time_duration", None),
                        link.get("time_type", None),
                    ],
                }
            )
    return db_data
