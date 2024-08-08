import requests
import datetime
from datetime import datetime

LONG = "16.545025"
LAT = "59.611366"
PROVIDER = "SMHI"
date_format = "%Y-%m-%dT%H:%M:%SZ"

def get_date_SMHI(weather_data: dict) -> datetime:
    datetime_str = weather_data["validTime"]
    return datetime.strptime(datetime_str, date_format)


def get_temperature_SMHI(weather_data: dict) -> float:
    for parameter in weather_data["parameters"]:
        if parameter["name"] == "t":
            return parameter["values"][0]


def get_precipitation_SMHI(weather_data: dict) -> bool:
    for parameter in weather_data["parameters"]:
        if parameter["name"] == "pcat":
            if parameter["values"][0] != 0:
                return True
            return False


def get_created_time_SMHI() -> datetime:
    datetime_string = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    return datetime.strptime(
        datetime_string, "%Y-%m-%d %H:%M:%S"
    )  # tar bort millisekunder från datetime


def get_latest_forecast_SMHI() -> list[dict]:
    url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.158/lat/58.5812/data.json"
    response = requests.get(url)
    json_data_dict = response.json()
    data = json_data_dict["timeSeries"][:24]
    created_date_obj = get_created_time_SMHI()
    weather_next_24h = []

    for weather_data in data:
        datetime_obj = get_date_SMHI(weather_data)
        weather_next_24h.append(
            {
                "created": (created_date_obj),
                "longitude": LONG,
                "latitude": LAT,
                "date": (datetime_obj.date()),
                "hour": (datetime_obj.hour + 2)
                % 24,  # lägg till 2 timmar så det blir svensk tid
                "temperature": get_temperature_SMHI(weather_data),
                "RainOrSnow": get_precipitation_SMHI(weather_data),
                "provider": PROVIDER,
            }
        )
    return weather_next_24h

