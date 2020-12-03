import json
import requests
from flask import current_app


# Send request to yelp API and return businesses result in an object
# Location default to Boston
# Return format see:
# https://www.yelp.com/developers/documentation/v3/business_search
def yelp_search(name, location="Boston"):

    # Load Yelp api interface
    url = "https://api.yelp.com/v3/businesses/search"

    # Initialize Yelp api authorization headers
    headers = {'Authorization': 'Bearer %s' %
                                current_app.config['YELP_API_KEY']}

    # Initialize payload that pass to yelp api
    payload = {"term": name, "location": location}

    # Request from Yelp Api, /businesses/search
    respond = requests.get(url, params=payload, headers=headers)

    # Decode json file
    ret = json.loads(respond.text)

    # Return result
    return ret
