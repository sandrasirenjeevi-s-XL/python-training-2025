import logging
def setup_logger(name:str,logfile:str,level=logging.DEBUG): #verbose mode
    formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler=logging.FileHandler(logfile)
    handler.setFormatter(formatter)
    logger=logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger
task_logger=setup_logger("app_logger","app_logger.log")