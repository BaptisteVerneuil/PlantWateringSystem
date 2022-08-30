import logging
import argparse
from datetime import datetime, timedelta

from data.get_sensor_data import get_sensor_data
from data.get_weather import get_precipitation
from data.moisture_forecast import forecast_moisture
from downlink_swm import send_info_pump
import config

logger = logging.getLogger("pws")


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_sensor", "-s", type=int, default=72,
                        help="Number of sensor entries")
    parser.add_argument("--days_forecast", "-d", type=int, default=1,
                        help="Number of days of weather data")
    parser.add_argument("--verbosity", "-v", type=int, default=20,
                        help="Set logging verbosity level (int), using the `logging` module's defaults: \
                            DEBUG=10, INFO=20, WARNING=30, ERROR=40. Defaults to 20.")
    args = parser.parse_args()


    # Setup logger
    config.setup_logger(logfile="pws.log", level=args.verbosity)
    logger.info("Using PlantWateringSystem version %s", config.__version__)

    # Getting past moisture
    past_moisture, dates_moisture = get_sensor_data(nb_entries=args.n_sensor)
    logger.info("Successful acquisition of sensor data")

    # Getting weather data
    now = datetime.now()
    last_date = now + timedelta(days=args.days_forecast)
    now = now.strftime("%Y-%m-%dT%H:%M") # Formatting
    last_date = last_date.strftime("%Y-%m-%dT%H:%M") # Formatting
    weather_data, dates_precipitation = get_precipitation(config.lat, config.lon, first_date=now, last_date=last_date)
    logger.info("Successful acquisition of weather data")

    # Code for simulating fake precipitations
    # weather_data[7:11] = [1, 2, 1.7, 1]


    # Forecasting moisture
    weights = [80*config.rate_weights**(len(past_moisture) - i) for i in range(len(past_moisture))] # The further apart the points are, the less weight they carry
    moisture_future, regr = forecast_moisture(past_moisture, [date.timestamp() for date in dates_moisture], weights, weather_data, [date.timestamp() for date in dates_precipitation])
    logger.info("Successful forecasting of moisture")

    # Code used for plotting the past and the forecasted moisture
    """
    import matplotlib.pyplot as plt; import matplotlib.dates
    plt.plot_date(matplotlib.dates.date2num(dates_moisture), past_moisture)
    plt.plot_date(matplotlib.dates.date2num(dates_precipitation), moisture_future)
    plt.title("Moisture of our plant today and tomorrow (in %)")
    plt.axhline(y = 40, color = 'r', linestyle = 'dashed', label = "Minimum critical moisture")
    plt.axhline(y = 80, color = 'b', linestyle = 'dashed', label = "Maximum critical moisture")
    plt.ylim(0, 100)
    plt.legend()
    plt.show()
    """

    # Giving order to the pump if needed, 2 criteria for watering the plant : 
    # 1) Current moisture is not too wet
    # 2) in the next 24H, soil moisture will be too dry

    current_moisture = past_moisture[-1] # current value = last value of the past

    if current_moisture < config.moisture_too_wet and min(moisture_future)[0] < config.moisture_too_dry:
        logger.info("Some pumping is required !")

        # We set the moisture the the target moisture
        moisture_to_add = config.target_moisture - min(moisture_future)

        # Sending the information to the pump
        success = send_info_pump(moisture_to_add)
        if success == 0 :
            logger.info("Successful sending of data to the pump")
        else :
            logger.info('\nSometing went wrong: HTTP Status: %s: %s' % (success[0], success[1]))
    else :
        logger.info("No pumping required")
    
    logger.info("--------------------------")