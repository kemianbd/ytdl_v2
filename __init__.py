from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
app = Blueprint('app', __name__)


def create_app():
    main = Flask(__name__)
    main.config['SECRET_KEY'] = '9348tuySDF4i9023u4'
    bootstrap.init_app(main)

    main.register_blueprint(app)

    return main

from . import views
