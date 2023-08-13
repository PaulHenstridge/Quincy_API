from mongoengine import Document, StringField

class Quote(Document):
    date = StringField()
    quote = StringField()
    quote_author = StringField()