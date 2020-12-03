from ..libs import yelpSearch
from .common.base import BaseResource
from ..schemas.yelp import YelpApiGetSchema

from flask import request


class YelpAPI(BaseResource):

    def get(self):
        # validate the requests parameters using schema
        params = self.validate_request(schema=YelpApiGetSchema, kwargs=request.values)  # noqa: E501

        # create response object
        respone = {"status": "ok"}

        # Request @name and @location from front end
        name = params.get("name")
        location = params.get("location")

        # Optional: radius
        # radius = request.args.get("radius")

        # Search via yelp_search method
        token = yelpSearch.yelp_search(name, location)

        # Print the returned token for debug use
        # TODO: remove when final integration
        print(token)

        # Return result to front end
        return token