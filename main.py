import requests

MY_LAT = 23.344101
MY_LNG = 85.309563

parameters = {

    "lat": MY_LAT,
    "lng": MY_LNG
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

