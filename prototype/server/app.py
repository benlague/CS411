from flask import Flask, request
import yaml
import os
import json
import requests

app = Flask(__name__)
creds = yaml.safe_load(open("creds.yaml", "r"))
url = "https://api.yelp.com/v3/businesses/search"
headers = {'Authorization': 'Bearer %s' % creds["API_KEY"]}


@app.route("/", methods=["GET"])
def index():
    # TODO: receive request from front end
    name = request.args.get("name")

    # Default to Boston
    location = "Boston"

    # payload that pass to api
    payload = {"term": name, "location": location}

    # TODO: request from Yelp Api, /businesses/search
    token = requests.get(url, params=payload, headers=headers)

    # print the returned token
    print(json.loads(token.text))
    ret = json.loads(token.text)
    # TODO: return result to front end

    return ret


if __name__ == "__main__":
    app.run(port=4000, debug=True)
