from os import environ
from settings import config_to_class

env = environ.get('ENV', 'production')

CFG = config_to_class(env)
