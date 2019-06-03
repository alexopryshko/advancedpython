import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('mylogger')

logger.error('error')
logger.warning('warning')
logger.info('information')
logger.debug('debug')

