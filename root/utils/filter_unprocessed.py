from ..models.email_link import EmailLink
from ..models.quote import Quote

def filter_unprocessed_links(link_data):
    unprocessed_links = []
    for entry in link_data:
        if not EmailLink.objects(link=entry["link"]).first():
            unprocessed_links.append(entry)
    return unprocessed_links


def filter_unprocessed_quotes(quote_data):
    unprocessed_quotes = []
    for entry in quote_data:
        if not Quote.objects(date=entry["date"]).first():
            unprocessed_quotes.append(entry)
    return unprocessed_quotes