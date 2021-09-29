import logging

import configs
from random_package import random_module
from utils import random_util

# In case `import configs` is cleaned by PyCharm's Reformat Code
configs.config_log()
logger = logging.getLogger(__name__)

random_util.do_something()
random_module.do_something()
logger.debug('Json format')
logger.info('info')
logger.warning('warning')

try:
    1 / 0
except ZeroDivisionError:
    logger.error('233', exc_info=True)
