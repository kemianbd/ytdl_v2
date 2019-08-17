from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
main = Blueprint('main', __name__)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9348tuySDF4i9023u4'
    bootstrap.init_app(app)

    app.register_blueprint(main)

    return app

from . import views
