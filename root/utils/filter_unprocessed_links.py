from ..models.email_link import EmailLink

def filter_unprocessed_links(link_data):
    unprocessed_links = []
    for entry in link_data:
        if not EmailLink.objects(link=entry["link"]).first():
            unprocessed_links.append(entry)
    return unprocessed_links