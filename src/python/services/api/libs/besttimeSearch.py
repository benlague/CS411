import json

from .cache import cache
from ..schemas.besttime import BestTimeForecastSchema

import requests
from flask import current_app


class BestTimeClient:

    NEW_FORECAST_ENDPOINT = "https://besttime.app/api/v1/forecasts"
    SECONDS_IN_WEEK = 604800

    def __init__(self):
        self.api_key_private = current_app.config['BESTTIME_API_KEY']
        self.besttime_forecast_schema = BestTimeForecastSchema()

    def new_forecast(self, venue_name: str, venue_address: str):
        params = {
            'api_key_private': self.api_key_private,
            'venue_name': venue_name,
            'venue_address': venue_address
        }

        response = requests.post(self.NEW_FORECAST_ENDPOINT, params=params)

        data = json.loads(response.text)

        return data

    def serialize_forecast(self, raw_forecast: dict):
        return self.besttime_forecast_schema.dump(raw_forecast)

    def get_forecast(self, venue_name: str, venue_address: str):
        venue_forecast_cache_key = f'besttime_forecast_{venue_name}_{venue_address}'  # noqa: E501

        if cache.has(venue_forecast_cache_key):
            venue_forecast = cache.get(venue_forecast_cache_key)
        else:
            venue_forecast = self.new_forecast(
                venue_name=venue_name,
                venue_address=venue_address
            )
            cache.set(
                key=venue_forecast_cache_key,
                value=venue_forecast,
                timeout=self.SECONDS_IN_WEEK
            )

        serialized_forecast = self.serialize_forecast(venue_forecast)

        return serialized_forecast
