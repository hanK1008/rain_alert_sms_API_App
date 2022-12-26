import requests

parameters = {
    "appid": "edc8e692ca16131a597b36e15a8c5260",
    "units": "metric",
    "exclude": "current,minutely,daily,alerts",
    # "lat": "18.687100",
    "lat": "49.314510",
    # "lon": "73.830250"
    "lon": "-122.855690"
}

api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_hourly_forcast = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
api_working = "https://api.openweathermap.org/data/2.8/onecall"


connection = requests.get(url=api_working, params=parameters)
connection.raise_for_status()
data = connection.json()

for n in range(12):
    weather_id = data["hourly"][n]["weather"][0]["id"]
    print(weather_id)
    if weather_id < 700:
        it_is_raining = True
        break
    else:
        it_is_raining = False


if it_is_raining:
    print("Bring and umbrella")
else:
    print("There will be no rain Today.")


