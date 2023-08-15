from mongoengine import connect
from ..models.email_link import EmailLink
from ..models.quote import Quote
from mongoengine import DoesNotExist

connect(db="quincy_api", host="localhost", port=27017)

def update_database(link_data, quote_data):

    for entry in link_data:
        try:
            db_record = EmailLink.objects.get(date_time=entry["date_time"])
            #print(f"data from {entry['date']} already saved.  DB up to date")
            
        except DoesNotExist:
            email_link = EmailLink(
                date=entry["date"],
                date_time=entry["date_time"],
                description=entry["description"],
                link=entry["link"],
                # quote=entry["quote"],
                length=entry["length"],
                length_mins=entry["length_mins"]
            )
            email_link.save()

    for entry in quote_data:
        quote = Quote(
            date=entry["date"],
            quote=entry["quote"],
            quote_author=entry["author"],
        )
        quote.save()