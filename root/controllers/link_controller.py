from flask import jsonify, request, send_from_directory, Blueprint, current_app
from mongoengine import Document, StringField, connect
from random import sample

from ..models.email_link import EmailLink
from ..utils.route_helpers.filter_db_results import apply_filters

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
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)
    min_length = request.args.get('min_length', None)
    max_length = request.args.get('max_length', None)


    query_set = EmailLink.objects()
    # apply filters
    query_set, error = apply_filters(query_set, start_date, end_date, min_length, max_length)

    if error:
        return jsonify({"error": error}), 400
    
    matching_links = list(query_set)
    
    links_list = [{
        'date': link.date,
        'link': link.link,
        'length': link.length,
        'description': link.description
    } for link in matching_links]

    return jsonify(links_list)



# get a random link
@link_blueprint.route('/links/random')
def get_random_link():
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)
    min_length = request.args.get('min_length', None)
    max_length = request.args.get('max_length', None)

    query_set = EmailLink.objects()
    # apply filters
    query_set, error = apply_filters(query_set, start_date, end_date, min_length, max_length)

    if error:
        return jsonify({"error": error}), 400
    
    random_link = sample(list(query_set), 1)[0]
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
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)
    min_length = request.args.get('min_length', None)
    max_length = request.args.get('max_length', None)

    query_set = EmailLink.objects(description__icontains=search_term)

    # apply filters
    query_set, error = apply_filters(query_set, start_date, end_date, min_length, max_length)

    if error:
        return jsonify({"error": error}), 400
    
    matching_links = list(query_set)

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
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)
    min_length = request.args.get('min_length', None)
    max_length = request.args.get('max_length', None)


    query_set = EmailLink.objects(tags__iexact=tag_to_search)

     # apply filters
    query_set, error = apply_filters(query_set, start_date, end_date, min_length, max_length)

    if error:
        return jsonify({"error": error}), 400
    
    matching_links = list(query_set)

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
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)
    min_length = request.args.get('min_length', None)
    max_length = request.args.get('max_length', None)

    query_set = EmailLink.objects(tags__icontains=term_to_search)
    
         # apply filters
    query_set, error = apply_filters(query_set, start_date, end_date, min_length, max_length)

    if error:
        return jsonify({"error": error}), 400
    
    matching_links = list(query_set)

    links_list = [{
        'date': link.date,
          'link': link.link,
            'length': link.length,
              'description': link.description
              } for link in matching_links]
    return jsonify(links_list)


# search links with any from a given list of tags ( make GET req to /links/search_by_tag_list?tags=tag1,tag2,tag3  )
@link_blueprint.route('/links/search_by_tags_list')
def search_by_tags_list():
    tags_string = request.args.get('tags', '')
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)
    min_length = request.args.get('min_length', None)
    max_length = request.args.get('max_length', None)

    # split and remove any empty strings
    tags_to_search = [tag.strip() for tag in tags_string.split(',')]
    print("searching tags:", tags_to_search)

    # Use the __in operator to match any of the tags in the list
    query_set = EmailLink.objects(tags__in=tags_to_search)

            # apply filters
    query_set, error = apply_filters(query_set, start_date, end_date, min_length, max_length)

    if error:
        return jsonify({"error": error}), 400
    
    matching_links = list(query_set)

    links_list = [{
        'date': link.date,
          'link': link.link,
            'length': link.length,
              'description': link.description
              } for link in matching_links]
    
    return jsonify(links_list)


# search links with all from a given list of tags ( make GET req to /links/search_by_tag_list_all?tags=tag1,tag2,tag3  )
@link_blueprint.route('/links/search_by_tags_list_all')
def search_by_tags_list_all():
    tags_string = request.args.get('tags', '')
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)
    min_length = request.args.get('min_length', None)
    max_length = request.args.get('max_length', None)

    # split and remove any empty strings
    tags_to_search = [tag.strip() for tag in tags_string.split(',')]
    print("searching tags:", tags_to_search)
    # Use the __in operator to match any of the tags in the list
    query_set = EmailLink.objects(tags__in=tags_to_search)
            # apply filters
    query_set, error = apply_filters(query_set, start_date, end_date, min_length, max_length)
 
    if error:
        return jsonify({"error": error}), 400
    
        # use python all() to return links where all tags are present
    matching_links = [link for link in query_set if all(tag in link.tags for tag in tags_to_search)]

    links_list = [{
        'date': link.date,
          'link': link.link,
            'length': link.length,
              'description': link.description
              } for link in matching_links]
    
    return jsonify(links_list)
