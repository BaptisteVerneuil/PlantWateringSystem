import requests
from datetime import datetime, timedelta

def get_precipitation(lat, lon, first_date, last_date):
    """
    Return the list of the hourly precipitation (in mm)
    ---------------------
    parameters:
    lat: str
        latitude of the selected location
    lon: str
        longitude of the selected location
    date: str
        selected date, in the format yyyy-mm-dd
    """
    url = "https://api.brightsky.dev/weather?lat={lat}&lon={lon}&date={first_date}&last_date={last_date}"

    resp = requests.get(url=url.format(lat=lat, lon=lon, first_date=first_date, last_date=last_date))
    data = resp.json() # Check the JSON Response Content documentation below

    list_precipitation = [data["weather"][i]["precipitation"] for i in range(len(data["weather"]))]
    list_date = [datetime.strptime(data["weather"][i]["timestamp"], "%Y-%m-%dT%H:%M:%S%z") for i in range(len(data["weather"]))] # We convert the string dates to datetime/datetime objects

    return list_precipitation, list_date

if __name__ == "__main__":

    # For testing purposes

    # Getting now's date
    now = datetime.now()
    last_date = now + timedelta(days=1)

    # Formatting
    now = now.strftime("%Y-%m-%dT%H:%M") 
    last_date = last_date.strftime("%Y-%m-%dT%H:%M") 
    
    # now = "2022-07-07" # It rained that day
    # last_date = "2022-07-08"

    precipitation_now,_ = get_precipitation(lat="48.121842", lon="11.600352", first_date = now, last_date=last_date)
    print(precipitation_now)
    import matplotlib.pyplot as plt
    plt.plot(precipitation_now)
    plt.title("Precipitations now (in mm)")
    plt.show()
