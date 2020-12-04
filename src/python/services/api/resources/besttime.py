from flask_login import login_required

from ..libs.besttimeSearch import besttime_search
from .common.base import BaseResource
from ..schemas.besttime import BestTimeApiGetSchema
from flask import request


class BestTimeAPI(BaseResource):
    # Make sure api is login protected
    method_decorators = [login_required]

    def get(self):
        # validate the requests parameters using schema
        params = self.validate_request(schema=BestTimeApiGetSchema, kwargs=request.values)  # noqa: E501

        # Request @name and @location from front end
        name = params.get("name")
        location = params.get("location")

        # Get besttime data using besttime_search method
        data = besttime_search(name, location)

        # Return besttime data to front end
        return data
