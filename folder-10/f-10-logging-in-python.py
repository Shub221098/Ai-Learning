# Folder 10: Video - 16 : Logging in python


import logging
# logging.basicConfig(format='%{asctime)s %{levelname}-8s [%(filename)s:%(lineno)d}] %{messages}s}', level=logging.DEBUG) # for pycharm

logger = logging.getLogger('test_logger')

logger.info('This will not show up.')
logger.warning('This will.')

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""