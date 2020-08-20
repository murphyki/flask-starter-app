import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # General config
    APP_NAME = os.environ.get('APP_NAME') or 'Flask Starter App'
    FLASK_APP = os.environ.get('FLASK_APP') or 'bootstrap.py'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'producion'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT') or 'True'
    LOG_FOLDER_NAME = os.environ.get('LOG_FOLDER_NAME') or '.logs'
    LOG_FILE_NAME = os.environ.get('LOG_FILE_NAME') or 'app.log'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@db:5432/database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
