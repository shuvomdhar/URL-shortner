import sqlite3
from config import Config
from datetime import datetime

class URLModel:
    def __init__(self):
        self.db_path = Config.DATABASE_PATH
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def create_url(self, original_url, short_code):
        """Create a new URL entry"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT INTO urls (original_url, short_code) VALUES (?, ?)',
            (original_url, short_code)
        )
        conn.commit()
        url_id = cursor.lastrowid
        conn.close()
        return url_id
    
    def get_url_by_short_code(self, short_code):
        """Get URL by short code"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'SELECT id, original_url, short_code, clicks, created_at FROM urls WHERE short_code = ?',
            (short_code,)
        )
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return {
                'id': result[0],
                'original_url': result[1],
                'short_code': result[2],
                'clicks': result[3],
                'created_at': result[4]
            }
        return None
    
    def increment_clicks(self, short_code):
        """Increment click count for a URL"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?',
            (short_code,)
        )
        conn.commit()
        conn.close()
    
    def get_recent_urls(self, limit=10):
        """Get recent URLs"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'SELECT original_url, short_code, clicks, created_at FROM urls ORDER BY created_at DESC LIMIT ?',
            (limit,)
        )
        results = cursor.fetchall()
        conn.close()
        
        return [
            {
                'original_url': row[0],
                'short_code': row[1],
                'clicks': row[2],
                'created_at': row[3]
            }
            for row in results
        ]
    
    def short_code_exists(self, short_code):
        """Check if short code already exists"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT id FROM urls WHERE short_code = ?', (short_code,))
        result = cursor.fetchone()
        conn.close()
        
        return result is not None

def init_db():
    """Initialize the database"""
    conn = sqlite3.connect(Config.DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            clicks INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()