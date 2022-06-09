import requests
import datetime as dt
from dateutil import tz

MY_LAT = 23.344101
MY_LNG = 85.309563

parameters = {

    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

# Convert from iso format to datetime format
sunrise = dt.fromisoformat(sunrise)
sunset = dt.fromisoformat(sunset)

# Tell the datetime object that it's in UTC time zone since datetime objects are 'naive' by default
sunrise = sunrise.replace(tzinfo=from_zone)
sunset = sunset.replace(tzinfo=from_zone)

# Convert time zone
sunrise = sunrise.astimezone(to_zone)
sunset = sunset.astimezone(to_zone)

# Extract the hour
sunrise_hr = sunrise.hour
sunset_hr = sunset.hour
