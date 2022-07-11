import logging
import argparse
from datetime import datetime, timedelta

from data.get_sensor_data import get_sensor_data
from data.get_weather import get_precipitation
import config

logger = logging.getLogger("pws")



if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_sensor", "-s", type=int, default=20,
                        help="Number of sensor entries")
    parser.add_argument("--n_weather", "-w", type=int, default=1,
                        help="Number of days of weather data")
    parser.add_argument("--verbosity", "-v", type=int, default=20,
                        help="Set logging verbosity level (int), using the `logging` module's defaults: \
                            DEBUG=10, INFO=20, WARNING=30, ERROR=40. Defaults to 20.")
    args = parser.parse_args()


    # Setup logger
    config.setup_logger(logfile="pws.log", level=args.verbosity)
    logger.info("Using PlantWateringSystem version %s", config.__version__)

    # Getting recent moisture
    recent_moisture, dates = get_sensor_data(nb_entries=args.n_sensor)

    # Getting weather data
    now = datetime.now()
    last_date = now + timedelta(days=args.n_weather)
    now = now.strftime("%Y-%m-%dT%H:%M") # Formatting
    last_date = last_date.strftime("%Y-%m-%dT%H:%M") # Formatting
    weather_data = get_precipitation(config.lat, config.lon, first_date=now, last_date=last_date)

    # Forecasting moisture
    # TODO

    # Giving order to the pump if needed
    # TODO