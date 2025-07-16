import string
import random
from models.url_model import URLModel
from config import Config

def generate_short_code(length=None):
    """Generate a random short code"""
    if length is None:
        length = Config.SHORT_CODE_LENGTH
    
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_unique_short_code():
    """Generate a unique short code that doesn't exist in database"""
    url_model = URLModel()
    
    while True:
        short_code = generate_short_code()
        if not url_model.short_code_exists(short_code):
            return short_code