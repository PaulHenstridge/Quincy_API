from .db.update_db import update_database
from .get_data import get_data


def main():
    link_data, quote_data = get_data()
    update_database(link_data, quote_data)


if __name__ == "__main__":
    main()
