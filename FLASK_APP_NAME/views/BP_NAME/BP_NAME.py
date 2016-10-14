from flask import Blueprint


bp = Blueprint('BP_NAME', __name__, url_prefix='/')


@bp.route('/')
def index():
    return "Hello"
