from flask import current_app, render_template
from app.services import bp

@bp.route('/services', methods=['GET'])
def index():
    current_app.logger.info('Processing servcies.index route...')
    return render_template('services.html', title='Services')
