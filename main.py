import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=34.99&longitude=137.01&hourly=temperature_2m&timezone=auto"
response = requests.get(url)
print(response.status_code)
data = response.json()
time = data["hourly"]["time"][15]
temp = data["hourly"]["temperature_2m"][15]
print(f"{time}の気温は{temp}度です。")