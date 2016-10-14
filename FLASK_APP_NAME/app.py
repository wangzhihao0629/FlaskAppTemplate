from flask import Flask
from werkzeug.utils import import_string

blueprints = [
    'xxx.xxx.xxx.xxx:bp'
]


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_pyfile('app.conf')
    app.secret_key = app.config['SECRET_KEY']

    for blueprint_name in blueprints:
        blueprint = import_string(blueprint_name)
        app.register_blueprint(blueprint)

    return app
