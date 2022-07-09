import os
import logging

from .logger_config import configure

configure(
	root_level=os.getenv('ROOT_LOG_LEVEL', 'INFO')
)

logger = logging.getLogger()