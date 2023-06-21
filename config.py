import os
from os import environ

class Config:
    USER_TOKEN = os.environ.get("USER_TOKEN", None)

    API_ID = int(environ['API_ID'])

    API_HASH = os.environ.get("API_HASH", None)
    
    SAVE_TO_CHNL = int(environ["SAVE_TO_CHNL"])
