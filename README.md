# URL Shortener

A Flask-based URL shortener with a clean web interface and RESTful API.

## Features

- Clean web interface for URL shortening
- RESTful API endpoints
- Click tracking and statistics
- SQLite database storage
- Proper project structure with separation of concerns

## Installation

1. Create project directory:
```bash
mkdir URL_shortener
cd URL_shortener
```

2. Create the file structure as shown above

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## API Endpoints

- `POST /api/shorten` - Shorten a URL
- `GET /api/stats/<short_code>` - Get URL statistics
- `GET /api/recent` - Get recent URLs

## Configuration

Edit `config.py` to customize:
- Database path
- Short code length
- Base URL
- Secret key

## Project Structure

```
url_shortener/
├── app.py                 # Application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── models/
│   ├── __init__.py
│   └── url_model.py      # Database model
├── routes/
│   ├── __init__.py
│   ├── main.py           # Main routes
│   └── api.py            # API routes
├── utils/
│   ├── __init__.py
│   ├── validators.py     # URL validation
│   └── generators.py     # Short code generation
├── templates/
│   ├── index.html        # Main page template
│   └── 404.html          # 404 error page
└── static/
    └── style.css         # CSS styles
```

## License

This project is open-source and available for educational use. Feel free to modify and distribute according to your needs.