import logging
import os

##### Logger #####

logfolder = "logs"
if not os.path.exists(logfolder):
    os.makedirs(logfolder)
    print('Log folder created')

logpath = os.path.join("logs", "server.log")
try:
    open(logpath, 'a').close()
except:
    # TODO add this to server logging
    raise

logger = logging.getLogger('log')
logger.setLevel(logging.INFO)

handler = logging.FileHandler(logpath)
handler.setFormatter(logging.Formatter(
    '%(levelname)s | %(filename)s | %(lineno)s | %(asctime)s :: %(message)s'))
logger.addHandler(handler)

##################

# Exceptions

class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
