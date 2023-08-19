from flask import jsonify, request, send_from_directory, Blueprint
from mongoengine import Document, StringField, connect
from ..models.email_link import EmailLink

# Create a Blueprint instance
link_blueprint = Blueprint('link_controller', __name__)

connect(db='quincy_api', host='localhost', port=27017)

#index
@link_blueprint.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

#get all
@link_blueprint.route('/links')
def get_all_links():
    all_links = EmailLink.objects()
    links_list = [{
        'date': link.date,
        'link': link.link,
        'length': link.length,
        'description': link.description
    } for link in all_links]

    return jsonify(links_list)


# search description text by making a GET request to /links/search?term=SEARCH_TERM.
@link_blueprint.route('/links/search')
def search_links():
    # Get search term query params
    search_term = request.args.get('term', '')  # Default to empty string if not provided
    
    # Find links where description contains search term 
    matching_links = EmailLink.objects(description__icontains=search_term)
    
    # Extract only the desired fields
    links_list = [{
        'date': link.date,
        'link': link.link,
        'length': link.length,
        'description': link.description
    } for link in matching_links]

    return jsonify(links_list)


