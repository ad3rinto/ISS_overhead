import requests
from datetime import datetime

MY_LAT = 53.3801  # Your latitude
MY_LONG = 2.1932  # Your longitude


def is_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response2.raise_for_status()
    data2 = response2.json()
    sunrise = int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data2["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # If the ISS is close to my current position
    if time_now >= sunset or time_now <= sunrise:
        return True


# and it is currently dark
def check_for_iss():
    if is_near() and is_night():
        print("Yhello")
    else:
        print("NFI")


# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
check_for_iss()
