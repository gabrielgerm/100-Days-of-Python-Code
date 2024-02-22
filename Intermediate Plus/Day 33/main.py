import requests
import smtplib
from datetime import datetime

def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude > MY_LAT-5 and iss_latitude < MY_LAT+5 and iss_longitude > MY_LONG-5 and iss_longitude < MY_LONG+5:
        return True
    else:
        return False
    
def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.split(" ")[1].split(":")[0]
    if current_hour >= sunset or current_hour <= sunrise:
        return True
    else:
        return False
    
    
MY_EMAIL = "zbindasilva@gmail.com"
MY_PASSWORD = "qede srib ebtl pykt"

MY_LAT = -23.694450 # Your latitude
MY_LONG = -46.565800 # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

if is_close() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(        
                from_addr=MY_EMAIL,
                to_addrs="zbindeoliveira@yahoo.com",
                msg=f"Subject:Look up nooow!!\n\nBro just look up..."
            )

