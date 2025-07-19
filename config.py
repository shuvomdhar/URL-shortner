import os

class Config:
    SECRET_KEY = 'secret-key'
    DATABASE_PATH = 'urls.db'
    SHORT_CODE_LENGTH = int(os.environ.get('SHORT_CODE_LENGTH', 6))
    BASE_URL = 'http://localhost:5000'