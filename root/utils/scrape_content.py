import requests
from bs4 import BeautifulSoup

def scrape_content(data):
    #for each element in data
    for article in data:
        print('ARTICLE!', article)
        response = requests.get(article["link"])

    #scrape the text content of the article
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all("article")
        print(f"there are {len(articles)} article elements")
        article_text = ''.join(article.text for article in articles)

    #pass the text to GPT to return content tags

    #save tags to DB
    

scrape_content([{
"date": "June 16, 2023",
"description": "C is the most widely-used programming language in the world. Even when you're coding in Python or JavaScript, you're still using C under the hood. One key reason why C is still so popular 50 years after its creation is its high performance. C directly interacts with computer hardware. One way it does this is through Pointers, which point to the location of data in the computer's physical memory. In this beginner's freeCodeCamp course on C programming, you'll learn about Pointers and key concepts like Passing By Reference, Passing By Value, Void Pointers, Arrays, and more.",
"length": "2hours",
"link": "https://www.freecodecamp.org/news/finally-understand-pointers-in-c/"
},
{
"date": "March 18, 2021",
"description": "This course will teach you fundamental data structures like arrays and linked lists. You'll then use these data structures to build common algorithms like Merge Sort and Quicksort.",
"length": "6hours",
"link": "https://www.freecodecamp.org/news/algorithms-and-data-structures-free-treehouse-course/"
}])
