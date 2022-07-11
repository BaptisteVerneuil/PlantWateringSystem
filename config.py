import logging
from logging.handlers import TimedRotatingFileHandler

__version__ = "0.1"


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