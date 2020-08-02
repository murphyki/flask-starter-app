from flask import current_app, render_template
from app.home import bp

@bp.route('/', methods=['GET'])
@bp.route('/home', methods=['GET'])
def index():
    current_app.logger.info('Processing home.index route...')
    return render_template('home.html')
