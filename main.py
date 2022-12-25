import requests

parameters = {
    "appid": "edc8e692ca16131a597b36e15a8c5260",
    "units": "metric",
    "exclude": "current,minutely,daily,alerts",
    "lat": "18.687100",
    "lon": "73.830250"
}

api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_hourly_forcast = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
api_working = "https://api.openweathermap.org/data/2.8/onecall"


connection = requests.get(url=api_working, params=parameters)
connection.raise_for_status()
data = connection.json()
print(data)

