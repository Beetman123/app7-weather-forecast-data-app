import requests


API_KEY = "d43c2f865be9eb74d4da60ec9f1"
"""
lat= 0
lon= 0
url = f"api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
"""


def get_data(place, forecast_days, kind):
    city_name_url = f"api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(city_name_url)
    data = response.json()
    filtered_data = data['list']
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]
    if kind == "Tempurature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    elif kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

