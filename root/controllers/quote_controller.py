from flask import jsonify, request, send_from_directory, Blueprint, current_app
from mongoengine import Document, StringField, connect
from random import sample

from ..models.quote import Quote
from ..utils.route_helpers.filter_db_results import apply_filters

# Create a Blueprint instance
quote_blueprint = Blueprint('quote_controller', __name__)

connect(db='quincy_api', host='localhost', port=27017)


#get all quotes
@quote_blueprint.route('/quotes')
def get_all_quotes():
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)

    query_set = Quote.objects()
    # apply filters
    query_set, error = apply_filters(query_set, start_date, end_date, min_length=0, max_length=0)

    if error:
        return jsonify({"error": error}), 400
    
    matching_quotes = list(query_set)
    
    quotes_list = [{
        'date': quote.date,
        'quote': quote.quote,
        'quote_author': quote.quote_author
    } for quote in matching_quotes]

    return jsonify(quotes_list)



# get a random quote
@quote_blueprint.route('/quotes/random')
def get_random_quote():
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)

    query_set = Quote.objects()
    # apply filters
    query_set, error = apply_filters(query_set, start_date, end_date, min_length=0, max_length=0)

    if error:
        return jsonify({"error": error}), 400
    
    quote = sample(list(query_set), 1)[0]
    quote_details = {
        'date': quote.date,
        'quote': quote.quote,
        'quote_author': quote.quote_author
    }
    return jsonify(quote_details)
