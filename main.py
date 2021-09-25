import json
import logging.config
import pathlib

from module_dir import random_module
from utils import random_util

with open(pathlib.Path(__file__).parent / 'configs' / 'log_config.json') as f:
    logging.config.dictConfig(json.load(f))
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
