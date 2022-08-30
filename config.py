import logging
from logging.handlers import TimedRotatingFileHandler

__version__ = "0.1"

# Parameters depending on the plant:
lat="48.121842"
lon="11.600352"
moisture_too_wet = 80
moisture_too_dry = 40
target_moisture = 65
area_plant = 0.01 # in m^2 (10cm*10cm)
conversion_moisture_volume = 400 # 1L of water = +400% of soil moisture # TODO
flow_rate_pump = 38 #mL/s

# Other parameters
rate_weights=0.885 # importance of measurements close to now ; if 1 run every 6h and 1 info every 10 minutes: 0.885**36 = 0.0123


# Setup project logger
def setup_logger(logfile: str = None, level: int = logging.INFO):
    logger = logging.getLogger(__package__)
    logger.setLevel(level)

    has_filehandler = False
    has_streamhandler = False
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            has_filehandler = True
        elif isinstance(handler, logging.StreamHandler):
            has_streamhandler = True
    if logfile and not has_filehandler:
        sh = TimedRotatingFileHandler(logfile, when="midnight")
    elif not has_streamhandler:
        sh = logging.StreamHandler()
    else:
        return
    sh.setLevel(level)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                                datefmt="%d-%m-%y %H:%M")
    sh.setFormatter(formatter)
    logger.addHandler(sh)