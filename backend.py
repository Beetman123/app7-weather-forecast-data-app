import requests


API_KEY = "99301d43c2f865be9eb74d4da60ec9f1"
"""
lat= 0
lon= 0
url = f"api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
"""


def get_data(place, forecast_days=None):
    test_url = "https://api.openweathermap.org/data/2.5/forecast?q=Tirana&appid=99301d43c2f865be9eb74d4da60ec9f1"
    city_name_url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(city_name_url)
    data = response.json()
    filtered_data = data['list']
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]
    return filtered_data

