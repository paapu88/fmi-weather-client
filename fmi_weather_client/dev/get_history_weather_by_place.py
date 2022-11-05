import fmi_weather_client as fmi
from fmi_weather_client.errors import ClientError, ServerError
import datetime
weather = fmi.weather_by_place_name(name="Harmaja, Helsinki")
if weather is not None:
        print(f"Current Temperature in {weather.place} is {weather.data.temperature}")

try:
    weather = fmi.past_weather_by_place_name(name="Harmaja, Helsinki",
                                             mytime=datetime.datetime(year=2022, month=10, day=27, hour=10,
                                                                      tzinfo=datetime.timezone.utc))
    if weather is not None:
        print(f"Temperature in {weather.place} is {weather.data.temperature}")
except ClientError as err:
    print(f"Client error with status {err.status_code}: {err.message}")
except ServerError as err:
    print(f"Server error with status {err.status_code}: {err.body}")