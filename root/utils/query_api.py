import os
import openai
import requests

def query_API(prompt):

    openai.organization =  os.getenv("OPENAI_ORG_KEY")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    model_list = openai.Model.list()

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
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 700,
        "temperature": 0
    }

    # Making the POST request
    response = requests.post(url, headers=headers, json=data).json()

    # Printing the response
    return(response["choices"][0]["message"]["content"])
   




