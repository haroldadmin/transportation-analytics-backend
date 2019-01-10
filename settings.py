# SQLAlchemy settings
import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask settings
FLASK_SERVER_NAME = 'localhost:3000'
FLASK_DEBUG = True  # Do not use debug mode in production

# JWT
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not JWT_SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY environment variable not defined")
