from mongoengine import Document, StringField, FloatField, DateTimeField, ListField

class EmailLink(Document):
        date = StringField()
        date_time = DateTimeField()
        description = StringField()
        link = StringField()
        tags = ListField()
        length = StringField()
        length_mins = FloatField()