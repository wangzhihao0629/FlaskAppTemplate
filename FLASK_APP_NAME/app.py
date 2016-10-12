from flask import Flask


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_pyfile('app.conf')
    app.secret_key = app.config['SECRET_KEY']
    return app
