import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # General config
    APP_NAME = os.environ.get('APP_NAME')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT') in ['true', 'True', 'yes']
    LOG_FOLDER_NAME = os.environ.get('LOG_FOLDER_NAME')
    LOG_FILE_NAME = os.environ.get('LOG_FILE_NAME')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Database config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') in ['true', 'True', 'yes']
    SQLALCHEMY_ECHO = os.environ.get('SQLALCHEMY_ECHO') in ['true', 'True', 'yes']
