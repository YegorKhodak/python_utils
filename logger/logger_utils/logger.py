import os
import logging
from logging.config import dictConfig


def configure(root_level=logging.INFO):
	dictConfig({
		'version': 1,
		'formatters': {
			'basic': {
				'format': '%(asctime)-25s %(levelname)-8s %(name)-8s %(message)s'
			},
			'extended': {
				'format': '%(asctime)-25s %(levelname)-8s %(name)-8s T:%(thread)-8s %(funcName)-20s %(message)s'
			}
		},
		'handlers': {
			'console': {
				'class': 'logging.StreamHandler',
				'formatter': 'basic',
				'level': logging.DEBUG
			}
		},
		'root': {
			'handlers': ['console'],
			'level': root_level
		}
	})

