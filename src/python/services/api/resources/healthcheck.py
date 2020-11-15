from flask.helpers import make_response
from .common.base import BaseResource
from ..schemas.healthcheck import HealthCheckGetSchema

from flask import request, jsonify


class HealthCheckAPI(BaseResource):

    def get(self):
        # validate the requests parameters using schema
        params = self.validate_request(schema=HealthCheckGetSchema, kwargs=request.values)  # noqa: E501

        # create response object
        respone = {"status": "ok"}

        # add the echo to the response if exists
        if "echo" in params:
            respone.update({"echo": params.get("echo")})

        # return response object and 200 ok status code
        return make_response(jsonify(respone), 200)
