from ..get_data import get_data
from mongoengine import connect

connect(db="quincy_api", host="localhost", port=27017)

from mongoengine import Document, StringField, ListField


class EmailLink(Document):
    date = StringField()
    description = StringField()
    link = StringField()
    length = ListField()


# class Quote(Document):


data = get_data()

EmailLink.objects.delete()

for entry in data:
    email_link = EmailLink(
        date=entry["date"],
        description=entry["description"],
        link=entry["link"],
        # quote=entry["quote"],
        length=entry["length"],
    )
    email_link.save()
