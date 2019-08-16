from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
main = Blueprint('main', __name__)


def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)

    app.register_blueprint(main)

    return app

from . import views
