# Quincy API

## Overview

Quincy API is a Flask-based web application that provides a suite of endpoints for querying a MongoDB database containing curated content from the FreeCodeCamp community, delivered since 2017 by emails from it's founder, Quincy Larson. 
As well as allowing for searches of the description contents, the application scrapes each article and uses AI to produce content tags for advanced searching.   It also offers filtering based on date and content duration.
The application features a simple front-end built with HTML, CSS, and JavaScript for easy testing and demonstration of the API's capabilities.

## Features

- **Searchable Tags**: Uses AI to generate searchable tags for each article.
- **Advanced Filters**: Allows for filtering by date and content length.
- **Random Content Retrieval**: Provides an endpoint for fetching random articles or quotes.
- **User-friendly Front-end**: A straightforward interface for testing the API.
- **Date and Time Conversion**: Converts human-readable dates to machine-friendly datetime objects for better filtering.
- **Inspirational Quotes**: A separate collection containing the motivational quotes that accompany Quincy's emails.

## Technologies

- Python
- Flask
- MongoDB
- BeautifulSoup
- OpenAI GPT-3.5turbo
- HTML, CSS, JavaScript

## Link Endpoints

- **`GET /links`**: Fetch all links.
- **`GET /links/random`**: Fetch a random link.
- **`GET /links/search?term=<SEARCH_TERM>`**: Search links by description.
- **`GET /links/search_by_tag?tag=<TAG>`**: Search links by tag.
- **`GET /links/search_by_tags_list?tags=<TAG1,TAG2,...>`**: Search for links containing ANY provided tag.
- **`GET /links/search_by_tags_lis_allt?tags=<TAG1,TAG2,...>`**: Search for links containing ALL provided tags.

## Quote Endpoints

- **`GET /quotes`**: Fetch all quotes.
- **`GET /quotes/random`**: Fetch a random quote.

## Acknowledgments

A huge shoutout to FreeCodeCamp and Quincy Larson for making all the data available that facilitated this project. Thanks to Sourabh Joshi who has maintained a record of Quincy Larson's emails in json format, and made it availabel on github - https://github.com/sourabh-joshi.  These weekly emails have been an endless source of inspiration and learning for me, and for the developer community.  I 'accidentally' learned so much while working with these fascinating articles!

## What I Learned

This project was all about diving deeper into Python development post-bootcamp. It provided an opportunity to explore the Python ecosystem, experiment combining Flask and MongoDB, and integrating an AI language model while developing a RESTful API.  Having some more time post-bootcamp to explore allowed for a more in-depth understanding of the underlying concepts, and an even greater appreciation for Python!

## Future Plans

- Add more advanced filtering options.
- Improve AI capabilities for tag generation.

## Get Started

To replicate the API in your local emvironment, you will need MongoDB, and an OpenAI API key.
First, clone the repository,

```bash
git clone git@github.com:PaulHenstridge/Quincy_API.git
cd quincy_api
pip install -r requirements.txt
```

then create the database,
```
use quincy_api
```

next, start the app with the --fetch-data flag. This will fetch, scrape and tag any article that is not already in the database.  Access to OpenAI API is required.
```bash
python3 run.py --fetch-data
```

To run the app without fetching data.  You can still search the database on the description content.
```bash
python3 run.py
```

Open your browser and navigate to  ```localhost:5000 ``` to start exploring the API!

## License

This project is open-source and available under the MIT License.

