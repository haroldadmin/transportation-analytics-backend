from flask import Blueprint, Flask

import settings
from api import api
from api.jwt_extension import jwt
from database import db

app = Flask(__name__)


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY
    flask_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = settings.JWT_ACCESS_TOKEN_EXPIRES
    flask_app.config['JWT_REFRESH_TOKEN_EXPIRES'] = settings.JWT_REFRESH_TOKEN_EXPIRES


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)

    jwt.init_app(flask_app)
    db.init_app(flask_app)


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    initialize_app(app)
    app.run(host="0.0.0.0", port=settings.PORT, debug=settings.FLASK_DEBUG)
