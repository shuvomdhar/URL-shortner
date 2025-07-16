from flask import Blueprint, request, jsonify
from models.url_model import URLModel
from utils.validators import is_valid_url, normalize_url
from utils.generators import generate_unique_short_code

api_bp = Blueprint('api', __name__)
url_model = URLModel()

@api_bp.route('/shorten', methods=['POST'])
def shorten_url():
    """API endpoint for shortening URLs"""
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    original_url = data['url'].strip()
    normalized_url = normalize_url(original_url)
    
    if not is_valid_url(normalized_url):
        return jsonify({'error': 'Invalid URL'}), 400
    
    # Generate unique short code
    short_code = generate_unique_short_code()
    
    # Create URL entry
    url_model.create_url(normalized_url, short_code)
    
    return jsonify({
        'original_url': normalized_url,
        'short_url': request.url_root + short_code,
        'short_code': short_code
    })

@api_bp.route('/stats/<short_code>')
def get_stats(short_code):
    """API endpoint for getting URL statistics"""
    url_data = url_model.get_url_by_short_code(short_code)
    
    if url_data:
        return jsonify(url_data)
    else:
        return jsonify({'error': 'URL not found'}), 404

@api_bp.route('/recent')
def get_recent_urls():
    """API endpoint for getting recent URLs"""
    recent_urls = url_model.get_recent_urls()
    return jsonify({'urls': recent_urls})