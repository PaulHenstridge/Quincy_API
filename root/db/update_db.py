from mongoengine import connect
from ..models.email_link import EmailLink
from ..models.quote import Quote
from mongoengine import DoesNotExist
from ..utils.filter_unprocessed_links import filter_unprocessed_links
from ..utils.add_content_tags import add_content_tags

connect(db="quincy_api", host="localhost", port=27017)

def update_database(link_data, quote_data):
    unprocessed_links = filter_unprocessed_links(link_data)
    tag_data = add_content_tags(unprocessed_links)

    for entry, tags in zip(unprocessed_links, tag_data):
  
        email_link = EmailLink(
            date=entry["date"],
            date_time=entry["date_time"],
            description=entry["description"],
            link=entry["link"],
            tags=tags,
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