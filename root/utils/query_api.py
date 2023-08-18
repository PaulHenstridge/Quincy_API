import os
import openai
import requests
import tiktoken
#tiktoken used to count tokems
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

#truncate text to max-token limit - adjust for larger model!
def truncate_text(text, max_tokens=2048):
    tokens = enc.encode(text)
    if len(tokens) <= max_tokens:
        return text
    truncated_tokens = tokens[ :max_tokens]
    truncated_text = enc.decode(truncated_tokens)
    return truncated_text

def query_API(article):
    trimmed_article = truncate_text(article)
    # openai.organization =  os.getenv("OPENAI_ORG_KEY")
    # openai.api_key = os.getenv("OPENAI_API_KEY")

    # model_list = openai.Model.list()

    # Endpoint URL
    url = "https://api.openai.com/v1/chat/completions"

    # Headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}" 
    }

    # Request data
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", 
             "content": """Your role is to summarise articles into searchable keywords. Articles will give an introduction to a lesson
                            for students of software development, coding, tech etc.  the keywords will be used to search the lessons by content, so 
                            should be consistent, short (1-2 words per keyword), and capture the key subject matter of interest to students. Prioritise technologies
                            e.g. React, Python, Node.js; concepts e.g. TDD, SOLID, design principles; associated activities e.g. interview prep, algorithms, deploying websites
                            webscrapers, blockchain etc.   return only a list of keywords.  DO not include any other response in the completion, except for the list of keywords,
                            seperated by commas.  e.g.  Javascript, Node.js, webcrawler, MongoDB, code-along"""},
            { "role": "user", "content": trimmed_article }
        ],
    }

    # Making the POST request
    response = requests.post(url, headers=headers, json=data).json()

    # Printing the response
    try:
        return response["choices"][0]["message"]["content"]
    except KeyError:
        print("Error: Unexpected response format:", response)
        return None  # or some default value or behavior

   




