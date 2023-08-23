import requests
from datetime import datetime

from .query_api import query_API
from .add_content_tags import add_content_tags

#this func allows the date to be parsed in either abbreviated or full word format
def flexible_strptime(date_str):
    formats = ["%b %d, %Y", "%B %d, %Y"] 
    for format in formats:
        try:
            return datetime.strptime(date_str, format)
        except ValueError:
            pass
    raise ValueError(f"time data {date_str!r} does not match any of the provided formats")

def get_data():
    
    response = requests.get(
        "https://raw.githubusercontent.com/sourabh-joshi/awesome-quincy-larson-emails/main/emails.json"
    )

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")

# testing data

#     data = {"emails":[{
# "date": "Aug 11, 2023",
# "links": [
# {
# "description": "freeCodeCamp has partnered with Harvard to bring you another mind-expanding CS50 course: Introduction to Artificial Intelligence with Python. You'll get broad exposure to Machine Learning theory: Optimization, Classification, Graph Search Algorithms, Reinforcement Learning, and more. You can code along at home and implement your own basic AIs using Python. This is a full university course that's completely self-paced and freely available. Enjoy.",
# "link": "https://www.freecodecamp.org/news/harvard-cs50s-ai-python-course",
# "order": "1",
# "time_duration": "12",
# "time_type": "hours"
# },
# {
# "description": "freeCodeCamp also published an end-to-end testing course. You'll learn QA Engineering with the powerful Cypress JavaScript library. Some of the concepts you'll pick up include Assertions, Command Chaining, Intercepts, and Multi-Page Testing. Every developer should be able to double as their own QA engineer, and to write their own tests. This course will show you how.",
# "link": "https://www.freecodecamp.org/news/mastering-end-to-end-testing-with-cypress-for-javascript-applications/",
# "order": "2",
# "time_duration": "3",
# "time_type": "hours"
# },
# {
# "description": "Like any good board game, JavaScript is easy to learn and hard to master. And in this advanced JS course, freeCodeCamp instructor Tapas Adhikary will teach you a wide range of function concepts. You'll learn about the Call Stack, Nested Functions, Callback Functions, Higher-Order Functions, Closures, and everyone's favorite: Immediately-Invoked Function Expressions -- also known as IIFE's (pronounced \"iffy\"). Put on your learning cap.",
# "link": "https://www.freecodecamp.org/news/mastering-javascript-functions-for-beginners/",
# "order": "3",
# "time_duration": "2",
# "time_type": "hours"
# },
# {
# "description": "Learn JavaScript by reverse-engineering your own JS utility library -- like the ever-popular Lodash library. In this tutorial, you'll learn how to hand-implement more than a dozen array methods, object methods, and math methods. This is excellent practice for brushing up on your JavaScript knowledge. And a lot of the code you write may make it into your other codebases.",
# "link": "https://www.freecodecamp.org/news/how-to-create-a-javascript-utility-library-like-lodash/",
# "order": "4",
# "time_duration": "45",
# "time_type": "minutes"
# },
# {
# "description": "When it comes to deploying your apps to production, there are a ton of options -- many of which don't cost a thing. freeCodeCamp contributor Ijeoma Igboagu compares several hosting platforms including Vercel and Netlify, and shares the strengths and weaknesses of each. She also shows you how to deploy to these services using Git.",
# "link": "https://www.freecodecamp.org/news/how-to-deploy-websites-and-applications/",
# "order": "5",
# "time_duration": "20",
# "time_type": "minutes"
# }
# ],
# "quote": "Computers are incredibly fast, accurate, and stupid. Humans are incredibly slow, inaccurate, and brilliant. Together they are powerful beyond imagination.",
# "quote_author": "widely attributed to Albert Einstein, as many profound quotes are"
# }]}

    quotes_data = []
    link_data = []
   

    for email in data["emails"]:
        quotes_data.append({
        "date": email.get("date", None),
        "quote": email.get("quote", None),
        "author": email.get("quote_author", None)
    })
        for link in email["links"]:
            link_data.append(
                {
                    "date": email.get("date", None),
                    "date_time":flexible_strptime(email.get("date", "Jan 1 2000")),
                    "quote": [email.get("quote", None), email.get("quote_author")],
                    "description": link.get("description", None),
                    "link": link.get("link", None),
                    "length": link.get("time_duration", ".") + link.get("time_type", "."),
                    "length_mins": float(link.get("time_duration", 0)) * (60 if link.get("time_type", None) == 'hours' else 1)  
                }
            )

    add_content_tags(link_data)
    return link_data, quotes_data
