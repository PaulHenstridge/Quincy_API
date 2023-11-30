from mongoengine import Document, StringField, DateTimeField

class Quote(Document):
    date = StringField()
    date_time = DateTimeField(null=True)
    quote = StringField()
    quote_author = StringField()