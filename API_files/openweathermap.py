import requests
import datetime
from datetime import datetime

LONG = "16.545025"
LAT = "59.611366"
PROVIDER = "openweathermap"
API_KEY = ""


def get_temperature_OWM(weather_dict: dict) -> float:
    return weather_dict["temp"]


def get_precipitation_OWM(weather_dict: dict) -> bool:
    if "rain" in weather_dict or "snow" in weather_dict:
        return True
    return False


def get_date_OWM(weather_dict: dict) -> datetime:
    time = weather_dict["dt"]
    return datetime.fromtimestamp(time)


def get_created_time_OWM() -> datetime:
    datetime_string = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    return datetime.strptime(
        datetime_string, "%Y-%m-%d %H:%M:%S"
    )  # tar bort millisekunder från datetime


def get_latest_forecast_OWM() -> list[dict]:
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LONG}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    json_data_dict = response.json()
    data = json_data_dict["hourly"][1:25]
    created = get_created_time_OWM()
    weather_next_24h = []
    for weather_data in data:
        datetime_obj = get_date_OWM(weather_data)
        weather_next_24h.append(
            {
                "created": created,
                "longitude": LONG,
                "latitude": LAT,
                "date": datetime_obj.date(),
                "hour": datetime_obj.hour,
                "temperature": get_temperature_OWM(weather_data),
                "RainOrSnow": get_precipitation_OWM(weather_data),
                "provider": PROVIDER,
            }
        )
    return weather_next_24h
