import requests
import datetime

def get_sensor_data(thing_id=80, datastream_id=269, nb_entries = 1):
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

    # We remove data before 10/07/2022 (uncalibrated sensor)
    url = "https://gi3.gis.lrg.tum.de/frost/v1.1/Things({thing_id})/Datastreams({datastream_id})/Observations?$orderby=phenomenonTime%20desc&$top={nb_entries}&$select=result,phenomenonTime&$filter=phenomenonTime ge 2022-07-10T00:00:00Z"
    #https://gi3.gis.lrg.tum.de/frost/v1.1/Things(80)/Datastreams(269)/Observations?$orderby=phenomenonTime%20desc&$top=1&$select=result,phenomenonTime
    
    resp = requests.get(url=url.format(thing_id=str(thing_id), datastream_id=str(datastream_id), nb_entries = str(nb_entries)))
    data = resp.json() # Check the JSON Response Content documentation below

    sensor_values = [data["value"][i]["result"] for i in range(len(data["value"]))]
    dates = [datetime.datetime.strptime(data["value"][i]["phenomenonTime"], "%Y-%m-%dT%H:%M:%S.%fZ") for i in range(len(data["value"]))]
    
    # Chronological order
    sensor_values.reverse()
    dates.reverse()

    return sensor_values, dates

if __name__ == "__main__":

    moisture_today, dates = get_sensor_data(nb_entries=1000)
    import matplotlib.pyplot as plt; import matplotlib.dates

    plt.plot_date(matplotlib.dates.date2num(dates), moisture_today)
    plt.title("Moisture of our plant today (in %)")
    plt.ylim(0, 100)
    plt.show()
