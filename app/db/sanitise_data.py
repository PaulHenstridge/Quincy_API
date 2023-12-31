import sys
import re

sys.path.append('/Users/paulhenstridge/Desktop/dev/python/quincy_api')

from mongoengine import connect
from app.models.email_link import EmailLink

connect(db="quincy_api", host="localhost", port=27017)


def contains_special_chars(tag):
    # Define a regex pattern to match any of the special characters
    pattern = re.compile(r'[.*+?|^(){}[\]\\]')
    return bool(pattern.search(tag))


# remove tags generated that are longer than 30 characters
upper_char_limit = 45
lower_char_limit = 30

def sanitise_data():
    removed_count = 0
    modified_count = 0
    cnt = 0

    for document in EmailLink.objects:
        for tag in document.tags:
            # if len(tag) > 30:
            #     cnt +=1
            #     print( cnt)
            # tag_length = len(tag)
            # if tag_length > upper_char_limit:
            #     document.update(pull__tags=tag)
            #     removed_count += 1
            #     print(f"Automatically removed {len(tag)} chars of waffle. Count: {removed_count}")
            # elif lower_char_limit <= tag_length <= upper_char_limit:
            #     user_input = input(f"Tag: '{tag}'.  Delete (D), Replace (R), or Keep (K)? ").lower()
            #     if user_input == 'd':
            #         document.update(pull__tags=tag)
            #         removed_count += 1
            #         print(f"{tag} removed. Count: {removed_count}")
            #     elif user_input == 'r':
            #         new_tag = input(f"Enter new tag to replace: ")
            #         document.update(pull__tags=tag)
            #         document.update(add_to_set__tags=new_tag)
            #         modified_count += 1
            #         print(f"{tag} replaced with {new_tag}. Modified count: {modified_count}")

            # Remove or replace tags containing special characters
            if contains_special_chars(tag):
                user_input = input(f"Tag: '{tag}'. Delete (D), Replace (R), or Keep (K)? ").lower()
                if user_input == 'd':
                    document.update(pull__tags=tag)
                    removed_count += 1
                    print(f"tag Deleted Count: {removed_count}")
                elif user_input == 'r':
                    new_tag = input(f"Enter new tag to replace: ")
                    document.update(pull__tags=tag)
                    document.update(add_to_set__tags=new_tag)
                    modified_count += 1
                    print(f"{tag} replaced with {new_tag} due to special characters. Modified count: {modified_count}")
    

sanitise_data()
