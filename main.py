import requests


def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=34.99&longitude=137.01&hourly=temperature_2m&timezone=auto"
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    return data


data = fetch_weather()
forecast_time = data["hourly"]["time"][15]
temp = data["hourly"]["temperature_2m"][15]
print(f"{forecast_time}の気温は{temp}度です。")