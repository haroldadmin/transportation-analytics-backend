# SQLAlchemy settings
import os
from datetime import timedelta

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask settings
# FLASK_SERVER_NAME = 'localhost:3000'
FLASK_DEBUG = True  # Do not use debug mode in production
PORT = 3000

# JWT
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not JWT_SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY environment variable not defined")

# Flask JWT settings
JWT_ACCESS_TOKEN_EXPIRES = timedelta(weeks=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(weeks=1)
