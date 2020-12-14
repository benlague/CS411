from .common.base import BaseResource
from ..libs.auth import login_required
from ..libs.besttimeSearch import BestTimeClient, BestTimeClientException
from ..schemas.besttime import BestTimeApiGetSchema

from flask import request
from flask_restful import abort


class BestTimeAPI(BaseResource):
    # Make sure api is login protected
    method_decorators = [login_required]

    def __init__(self):
        self.besttime_client = BestTimeClient()

    def get(self):
        # validate the requests parameters using schema
        params = self.validate_request(schema=BestTimeApiGetSchema, kwargs=request.values)  # noqa: E501

        # Request @name and @location from front end
        venue_name = params.get("name")
        venue_address = params.get("location")
        
        # Get besttime data
        try:
            venue_forecast = self.besttime_client.get_forecast(
                venue_name=venue_name,
                venue_address=venue_address
            )
        except BestTimeClientException as exc:
            return abort(503, message=exc)

        # Return besttime data to front end
        return venue_forecast
