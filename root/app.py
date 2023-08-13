from .db.update_db import update_database
from .utils.get_data import get_data
from flask import Flask

app = Flask(__name__)
from .controllers import link_controller

def main():
    link_data, quote_data = get_data()
    update_database(link_data, quote_data)


if __name__ == "__main__":
    # main()
    app.run(debug=True)
