# Configuration settings for the application

import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///app.db'
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL') or 'INFO'

# Additional configurations can be added here
