from .common.base import BaseSchema

from marshmallow import fields


class BestTimeApiGetSchema(BaseSchema):
    """ /api/BestTimeAPI - GET

    Parameters:
     - name (str)
     - location (str)
    """
    name = fields.Str(required=True)
    location = fields.Str(required=True)
