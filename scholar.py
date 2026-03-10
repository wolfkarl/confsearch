from os import kill

import requests
import json

def fetch_papers(query):
    PUBLICATION_TYPES = ['Review', 'JournalArticle', 'Conference']
    FIELDS =  [
        'title',
        'authors.name',
        'url',
        'publicationDate',
        'citationCount',
        'venue',
        'year',
    ]


    # Specify the search term
    # query = 'sustainable'

    # Define the API endpoint URL
    url = "http://api.semanticscholar.org/graph/v1/paper/search/bulk"

    # Define the query parameters
    query_params = {
        "query": query,
        "fields": ",".join(FIELDS),
        "venue": "ICSOC,EDOC,ICSA",
        # "year": "2023-"
        "publicationTypes": ",".join(PUBLICATION_TYPES),
        "limit": 10,
    }

    # # Directly define the API key (Reminder: Securely handle API keys in production environments)
    # api_key = "your api key goes here"  # Replace with the actual API key
    #
    # # Define headers with API key
    # headers = {"x-api-key": api_key}

    # Send the API request
    response = requests.get(url, params=query_params).json()
    return response
