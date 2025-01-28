import os

class Config:
    # General settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret@key')
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'  # Enable debugging mode
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')  # Set logging level
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://admin:red@localhost:5432/iot_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis settings (if applicable)
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
    
    # File upload settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit upload size to 16 MB

    # Other settings
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')