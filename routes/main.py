from flask import Blueprint, request, redirect, render_template, url_for
from models.url_model import URLModel
from utils.validators import is_valid_url, normalize_url
from utils.generators import generate_unique_short_code

main_bp = Blueprint('main', __name__)
url_model = URLModel()

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('url', '').strip()
        
        if not original_url:
            return render_template('index.html', error="Please enter a URL")
        
        # Normalize and validate URL
        normalized_url = normalize_url(original_url)
        if not is_valid_url(normalized_url):
            return render_template('index.html', error="Please enter a valid URL")
        
        # Generate unique short code
        short_code = generate_unique_short_code()
        
        # Create URL entry
        url_model.create_url(normalized_url, short_code)
        
        short_url = request.url_root + short_code
        recent_urls = url_model.get_recent_urls()
        
        return render_template(
            'index.html',
            short_url=short_url,
            original_url=normalized_url,
            recent_urls=recent_urls
        )
    
    # GET request - show form with recent URLs
    recent_urls = url_model.get_recent_urls()
    return render_template('index.html', recent_urls=recent_urls)

@main_bp.route('/<short_code>')
def redirect_to_url(short_code):
    url_data = url_model.get_url_by_short_code(short_code)
    
    if url_data:
        url_model.increment_clicks(short_code)
        return redirect(url_data['original_url'])
    else:
        return render_template('404.html'), 404