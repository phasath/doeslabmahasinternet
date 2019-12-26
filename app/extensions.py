from pymongo import MongoClient
from os import environ
from settings import config_to_class

env = environ.get('ENV', 'production')

CFG = config_to_class(env)
MONGO = MongoClient(CFG.MONGODB_URI)
labmaDB = MONGO.get_default_database()
labmaColl = labmaDB['labma']