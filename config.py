import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    APP_NAME = os.environ.get('APP_NAME') or 'Flask Starter App'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT') or 'True'
    LOG_FOLDER_NAME = os.environ.get('LOG_FOLDER_NAME') or '.logs'
    LOG_FILE_NAME = os.environ.get('LOG_FILE_NAME') or 'app.log'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
