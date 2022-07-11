import logging
import argparse

from data.get_sensor_data import get_sensor_data
from data.get_weather import get_precipitation
import config

logger = logging.getLogger("cymohand")



if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--sensor", "-s", type=int, default=20,
                        help="Number of sensor entries")
    parser.add_argument("--verbosity", "-v", type=int, default=20,
                        help="Set logging verbosity level (int), using the `logging` module's defaults: \
                            DEBUG=10, INFO=20, WARNING=30, ERROR=40. Defaults to 20.")
    args = parser.parse_args()


    # Setup logger
    config.setup_logger(logfile="cymohand.log", level=args.verbosity)

    logger.info("Using PlantWateringSystem version %s", config.__version__)


    recent_moisture, dates = get_sensor_data(nb_entries=args.sensor)
    recent_moisture.reverse()

    print(recent_moisture)

# import matplotlib.pyplot as plt; import matplotlib.dates