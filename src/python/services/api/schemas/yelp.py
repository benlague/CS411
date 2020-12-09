from .common.base import BaseSchema

from marshmallow import fields


class YelpApiGetSchema(BaseSchema):
    """ /api/yelp - GET

    Parameters:
     - name (str)
     - location (str)
    """
    name = fields.Str(required=True)
    location = fields.Str(required=True)
