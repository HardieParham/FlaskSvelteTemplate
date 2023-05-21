from flask import Blueprint

bp_financials = Blueprint('bp', __name__, url_prefix='/test')

@bp_financials.route('/')
def index():
    return '<h1>TEST</h1>'