from ..app import app
from mongoengine import Document, StringField, connect
from models.email_link import EmailLink
from flask import jsonify


connect(db='quincy_api', host='localhost', port=27017)


@app.route('/')
def index():
    return "the home page with docs, routes etc here  BOOBS"

@app.route('/links')
def get_all_links():
    all_links = EmailLink.objects()
    print(all_links)
    return jsonify(all_links)

    