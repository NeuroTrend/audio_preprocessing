import logging.config
import yaml
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(current_dir, 'logging_config.yaml')
print(config_path)
with open(config_path, 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

env = os.getenv('ENV', 'development')

logger = logging.getLogger(env)