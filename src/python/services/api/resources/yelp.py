from ..libs.auth import login_required
from ..libs.yelpSearch import yelp_search, YelpException
from .common.base import BaseResource
from ..schemas.yelp import YelpApiGetSchema

from flask import request
from flask_restful import abort


class YelpAPI(BaseResource):
    # Make sure api is login protected
    method_decorators = [login_required]

    def get(self):
        # validate the requests parameters using schema
        params = self.validate_request(schema=YelpApiGetSchema, kwargs=request.values)  # noqa: E501

        # Request @name and @location from front end
        name = params.get("name")
        location = params.get("location")

        # Search via yelp_search method
        try:
            yelp_data = yelp_search(name, location)
        except YelpException as exc:
            return abort(503, message=exc)

        # Return result to front end
        return yelp_data
