import requests

def get_precipitation(lat, lon, date):
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
    url = "https://api.brightsky.dev/weather?lat={lat}&lon={lon}&date={date}"

    resp = requests.get(url=url.format(lat=lat, lon=lon, date=date))
    data = resp.json() # Check the JSON Response Content documentation below

    return [data["weather"][i]["precipitation"] for i in range(len(data["weather"]))]

def test_precipitation():

    # Getting today's date
    from datetime import date
    today = date.today()
    today = today.strftime("%Y-%m-%d") # formatting
    # today = "2022-07-07" # It rained that day

    precipitation_today = get_precipitation(lat="48.121842", lon="11.600352", date = today)
    import matplotlib.pyplot as plt
    plt.plot(precipitation_today)
    plt.title("Precipitations today (in mm)")
    plt.show()
    return None

# test_precipitation()