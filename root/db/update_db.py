from mongoengine import connect
from ..models.email_link import EmailLink
from ..models.quote import Quote

connect(db="quincy_api", host="localhost", port=27017)

def update_links_collection(link, tag_list):
        
        email_link = EmailLink(
            date=link["date"],
            date_time=link["date_time"],
            description=link["description"],
            link=link["link"],
            tags=tag_list,
            length=link["length"],
            length_mins=link["length_mins"]
        )
        email_link.save()
        print("link saved")



def update_quotes_collection(quote_data):
    count = 1
    for entry in quote_data:
        quote = Quote(
            date=entry["date"],
            date_time=entry["date_time"],
            quote=entry["quote"],
            quote_author=entry["author"],
        )
        quote.save()
        print(f"quote {count} of {len(quote_data)} saved")
        count+=1
        if count > len(quote_data):
            print("All Quote Data saved To DB. Yay!")