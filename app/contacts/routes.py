from flask import current_app, render_template
from app.contacts import bp

@bp.route('/contacts', methods=['GET'])
def index():
    current_app.logger.info('Processing contacts.index route...')
    return render_template('contacts.html', title='Contacts')
