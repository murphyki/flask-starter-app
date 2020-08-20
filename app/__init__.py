import logging
import os
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.home import bp as home_bp
from app.services import bp as services_bp
from app.contacts import bp as contacts_bp

db = SQLAlchemy()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    if app.config['LOG_TO_STDOUT'] == 'True':
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    else:
        log_folder_name = app.config['LOG_FOLDER_NAME']
        log_file_name = app.config['LOG_FILE_NAME']
        log_file_path = os.path.join(log_folder_name, log_file_name)

        if not os.path.exists(log_folder_name):
            os.mkdir(log_folder_name)

        file_handler = RotatingFileHandler(
            log_file_path, 
            maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    with app.app_context():
        db.create_all()
        app.register_blueprint(home_bp)
        app.register_blueprint(services_bp)
        app.register_blueprint(contacts_bp)

    app.logger.setLevel(logging.INFO)
    app.logger.info('{0} started...'.format(app.config['APP_NAME']))
    app.logger.info('Logging to {0}...'.format('stdout' if app.config['LOG_TO_STDOUT'] == 'True' else 'log file'))

    return app
