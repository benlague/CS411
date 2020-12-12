from datetime import datetime
from pytz import timezone

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


class BestTimeDayInfoSchema(BaseSchema):
    day_int = fields.Int()
    day_text = fields.Str()
    venue_open = fields.Int()
    venue_closed = fields.Int()


class BestTimeDayAnalysisSchema(BaseSchema):
    day_raw = fields.List(fields.Int())
    day_info = fields.Nested(BestTimeDayInfoSchema)
    busy_hours = fields.List(fields.Int())
    quiet_hours = fields.List(fields.Int())


class BestTimeForecastSchema(BaseSchema):
    daily_forecast = fields.List(
        fields.Nested(BestTimeDayAnalysisSchema),
        attribute='analysis'
    )
    today_forecast = fields.Method(serialize='dump_today_forecast')

    def dump_today_forecast(self, besttime_forecast):
        venue_timezone = besttime_forecast['venue_info'].get(
            'venue_timezone',
            'America/New_York'
        )
        tz = timezone(venue_timezone)
        today_day_int = datetime.now(tz=tz).weekday()
        today_forecast_data = next(
            day_forecast for day_forecast in besttime_forecast['analysis'] if
            int(day_forecast['day_info']["day_int"]) == today_day_int
        )
        return BestTimeDayAnalysisSchema().dump(today_forecast_data)