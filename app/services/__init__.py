from flask import Blueprint

bp = Blueprint('services', __name__, template_folder='templates')

from app.services import routes
