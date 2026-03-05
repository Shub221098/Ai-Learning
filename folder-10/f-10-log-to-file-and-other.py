# Folder 10: Video - 17 : Logging to a file and other features in python

import logging
logging.basicConfig(
    format: '%{asctime)s %{levelname}-8s [%(filename)s:%(lineno)d}] %{messages}s}'
    datefmt: '%d-%m-%Y %H:%M:%S',
    level:logging.DEBUG,
    filename:'logs.txt'
)

logger = logging.getLogger('books')

logger.info('This will not show up.')
logger.warning('This will.')
logger.debug('This is a debug message.')
logger.critical('A critical error occured.')

logger = logging.getLogger('books.database')