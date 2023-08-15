from .db.update_db import update_database
from .utils.get_data import get_data
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()  # This loads environment variables from .env file

app = Flask(__name__)
from .controllers import link_controller

def main():
    link_data, quote_data = get_data()
    update_database(link_data, quote_data)
    app.run(debug=True)


    
