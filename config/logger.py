import logging.config
import yaml
import os

# Load the config file
with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

env = os.getenv('ENV', 'development')

logger = logging.getLogger('development')