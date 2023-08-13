from mongoengine import Document, StringField, FloatField, DateTimeField

class EmailLink(Document):
        date = StringField()
        date_time = DateTimeField()
        description = StringField()
        link = StringField()
        length = StringField()
        length_mins = FloatField()