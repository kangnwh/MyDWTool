import logging

def get_logger(filename,loggername='log'):
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(filename)
    ch = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(funcName)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    #logger.debug('This is debug message')
    #logger.info('This is info message')
    #logger.warning('This is warning message')
    return logger