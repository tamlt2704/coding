import os
import uuid

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or str(uuid.uuid1())
