from mongoengine import connect

connect(db="quincy_api", host="localhost", port=27017)

from mongoengine import Document, StringField, FloatField


def update_database(link_data, quote_data):
    class EmailLink(Document):
        date = StringField()
        description = StringField()
        link = StringField()
        length = StringField()
        length_mins = FloatField()

    class Quote(Document):
        date = StringField()
        quote = StringField()
        quote_author = StringField()

    for entry in link_data:
        email_link = EmailLink(
            date=entry["date"],
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