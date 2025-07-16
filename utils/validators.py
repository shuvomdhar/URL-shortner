from urllib.parse import urlparse

def is_valid_url(url):
    """Validate if a URL is properly formatted"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def normalize_url(url):
    """Add http:// if not present"""
    if not url.startswith(('http://', 'https://')):
        return 'http://' + url
    return url