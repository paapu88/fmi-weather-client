import datetime
from typing import Optional

import asyncio

from fmi_weather_client import myhttp
from fmi_weather_client.models import Weather
from fmi_weather_client.parsers import forecast as forecast_parser


def weather_by_coordinates(lat: float, lon: float) -> Optional[Weather]:
    """
    Get the latest weather information by coordinates.

    :param lat: Latitude (e.g. 25.67087)
    :param lon: Longitude (e.g. 62.39758)
    :return: Latest weather information if available; None otherwise
    """
    response = http.request_weather_by_coordinates(lat, lon)
    forecast = forecast_parser.parse_forecast(response)

    if len(forecast.forecasts) == 0:
        return None

    weather_state = forecast.forecasts[-1]
    return Weather(forecast.place, forecast.lat, forecast.lon, weather_state)


async def async_weather_by_coordinates(lat: float, lon: float) -> Optional[Weather]:
    """
    Get the latest weather information by coordinates asynchronously.

    :param lat: Latitude (e.g. 25.67087)
    :param lon: Longitude (e.g. 62.39758)
    :return: Latest weather information if available; None otherwise
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, weather_by_coordinates, lat, lon)


def weather_by_place_name(name: str) -> Optional[Weather]:
    """
    Get the latest weather information by place name.

    :param name: Place name (e.g. Kaisaniemi, Helsinki)
    :return: Latest weather information if available; None otherwise
    """
    response = http.request_weather_by_place(name)
    #print(f"present response: {response}")

    forecast = forecast_parser.parse_forecast(response)
    if len(forecast.forecasts) == 0:
        return None

    weather_state = forecast.forecasts[-1]
    return Weather(forecast.place, forecast.lat, forecast.lon, weather_state)

def past_weather_by_place_name(name: str, mytime:datetime.datetime) -> Optional[Weather]:
    """
    Get the laweather information by place name.

    :param name: Place name (e.g. Kaisaniemi, Helsinki)
    :param mytime: Time of the past weather
    :return: Latest weather information if available; None otherwise
    """
    response = http.request_past_weather_by_place(place=name, mytime=mytime)
    #print(f"past response: {response}")
    forecast = forecast_parser.parse_forecast(response)
    if len(forecast.forecasts) == 0:
        return None

    weather_state = forecast.forecasts[-1]
    return Weather(forecast.place, forecast.lat, forecast.lon, weather_state)


async def async_weather_by_place_name(name: str) -> Weather:
    """
    Get the latest weather information by place name asynchronously.

    :param name: Place name (e.g. Kaisaniemi, Helsinki)
    :return: Latest weather information if available, None otherwise
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, weather_by_place_name, name)


def forecast_by_place_name(name: str, timestep_hours: int = 24):
    """
    Get the latest forecast by place name.
    :param name: Place name
    :param timestep_hours: Hours between forecasts
    :return: Latest forecast
    """
    response = http.request_forecast_by_place(name, timestep_hours)
    return forecast_parser.parse_forecast(response)


async def async_forecast_by_place_name(name: str, timestep_hours: int = 24):
    """
    Get the latest forecast by place name asynchronously.
    :param name: Place name
    :param timestep_hours: Hours between forecasts
    :return: Latest forecast
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, forecast_by_place_name, name, timestep_hours)


def forecast_by_coordinates(lat: float, lon: float, timestep_hours: int = 24):
    """
    Get the latest forecast by coordinates
    :param lat: Latitude (e.g. 25.67087)
    :param lon: Longitude (e.g. 62.39758)
    :param timestep_hours: Hours between forecasts
    :return: Latest forecast
    """
    response = http.request_forecast_by_coordinates(lat, lon, timestep_hours)
    return forecast_parser.parse_forecast(response)


async def async_forecast_by_coordinates(lat: float, lon: float, timestep_hours: int = 24):
    """
    Get the latest forecast by coordinates
    :param lat: Latitude (e.g. 25.67087)
    :param lon: Longitude (e.g. 62.39758)
    :param timestep_hours: Hours between forecasts
    :return: Latest forecast
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, forecast_by_coordinates, lat, lon, timestep_hours)
