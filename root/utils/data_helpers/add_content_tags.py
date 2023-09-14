import time
import tiktoken
from .scrape_content import scrape_content
from .query_api import query_API
from ...db.update_db import update_links_collection

#tiktoken used to count tokems
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

def add_content_tags(link_data):
    # adding rate limiter
    token_limit_per_minute = 90000
    tokens_this_minute = 0
    start_time = time.time()
    current_minute = int(time.time() // 60)
    tags_lists = []
    count = 1
    for link in link_data:
        article_text = scrape_content(link["link"])
        if article_text is not None:
            token_count = len(enc.encode(article_text))

            elapsed_time_this_minute = (time.time() - start_time) % 60

            # Check if we are in a new minute and reset counter if needed
            new_minute = int(time.time() // 60)
            if new_minute != current_minute:
                print(f"{tokens_this_minute} tokens this passed minute")
                tokens_this_minute = 0
                current_minute = new_minute

            # Check if we need to wait for the next minute
            if tokens_this_minute + token_count > token_limit_per_minute:
                elapsed_time_this_minute = (time.time() - start_time) % 60
                time_to_next_minute = 60 - elapsed_time_this_minute
                print(f"rate limiter pausing for {time_to_next_minute} secs")
                time.sleep(time_to_next_minute)
                tokens_this_minute = 0
                current_minute = int(time.time() // 60)   

            tokens_this_minute += token_count
            AI_response = query_API(article_text)

            print(AI_response)

            # convert to list
            tag_list = [keyword.strip() for keyword in AI_response.split(',')]


            # pass link_data and tag_list to update() get it saved immediately

            # update_links_collection(link, tag_list)
            # print(f"link {count} of {len(link_data)} saved")
            # count+=1
