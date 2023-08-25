from flask import jsonify, request, send_from_directory, Blueprint, current_app
from mongoengine import Document, StringField, connect
from random import sample

from ..models.email_link import EmailLink

# Create a Blueprint instance
link_blueprint = Blueprint('link_controller', __name__)

connect(db='quincy_api', host='localhost', port=27017)


#index - serving home page
@link_blueprint.route('/')
def index():
    return send_from_directory(current_app.static_folder, 'index.html')



#get all links
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



# get a random link
@link_blueprint.route('/links/random')
def get_random_link():
    links_list = list(EmailLink.objects())
    random_link = sample(links_list, 1)[0]
    link_details = {
        'date': random_link.date,
        'link': random_link.link,
        'length': random_link.length,
        'description': random_link.description
    }
    return jsonify(link_details)



# search description text ( make a GET request to /links/search?term=SEARCH_TERM )
@link_blueprint.route('/links/search')
def search_links():
    search_term = request.args.get('term', '') 
    matching_links = EmailLink.objects(description__icontains=search_term)

    links_list = [{
        'date': link.date,
        'link': link.link,
        'length': link.length,
        'description': link.description
    } for link in matching_links]

    return jsonify(links_list)


# search by tag
@link_blueprint.route('/links/search_by_tag')
def search_links_by_tag():
    tag_to_search = request.args.get('tag', '')
    matching_links = EmailLink.objects(tags__iexact=tag_to_search)
    links_list = [{
        'date': link.date,
          'link': link.link,
            'length': link.length,
              'description': link.description
              } for link in matching_links]
    return jsonify(links_list)


# search for a term contained within a tag
@link_blueprint.route('/links/search_by_tag_partial')
def search_links_by_tag_partial():
    term_to_search = request.args.get('term', '')
    matching_links = EmailLink.objects(tags__icontains=term_to_search)
    links_list = [{
        'date': link.date,
          'link': link.link,
            'length': link.length,
              'description': link.description
              } for link in matching_links]
    return jsonify(links_list)


# search by a list of tags ( make GET req to /links/search_by_tag_list?tags=tag1,tag2,tag3  )
@link_blueprint.route('/links/search_by_tag_list')
def search_by_tags_list():
    tags_string = request.args.get('tags', '')
    tags_to_search = tags_string.split(',')
    # Use the __in operator to match any of the tags in the list
    matching_links = EmailLink.objects(tags__in=tags_to_search)
    links_list = [{
        'date': link.date,
          'link': link.link,
            'length': link.length,
              'description': link.description
              } for link in matching_links]
    
    return jsonify(links_list)
