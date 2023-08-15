from flask import Flask
import os
from dotenv import load_dotenv

 # load environment variables from .env file
load_dotenv()

from .db.update_db import update_database
from .utils.get_data import get_data
from .utils.query_api import query_API


app = Flask(__name__)
from .controllers import link_controller

def main():
    link_data, quote_data = get_data()
    update_database(link_data, quote_data)
    query_API()
    app.run(debug=True)

    
