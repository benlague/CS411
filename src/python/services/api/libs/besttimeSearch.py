import json
import requests
from flask import current_app


# 1. Sends forecast request to besttime API.
# 2. Returns a JSON file of all besttime data on the venue.
# Return format see:
# https://documentation.besttime.app/?python#new-forecast
def besttime_search(name, location):
    url = "https://besttime.app/api/v1/forecasts"

    params = {
        'api_key_private': current_app.config['BESTTIME_API_KEY'],
        'venue_name': name,
        'venue_address': location
    }

    response = requests.request("POST", url, params=params)

    data = json.loads(response.text)

    return data
