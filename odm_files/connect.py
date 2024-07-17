from mongoengine import *
from config.config import config

connect(db=config.get('DB_NAME'), host=config.get('DB_URL'))

