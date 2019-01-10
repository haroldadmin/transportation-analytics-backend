from werkzeug.security import generate_password_hash, check_password_hash

from database import db


class UserModel(db.Model):
    __tablename__ = "users"

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.set_password(password)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    requests = db.relationship("RouteRequestModel", backref="user", lazy=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)

    def set_password(self, password_plain_text):
        self.password_hash = generate_password_hash(password_plain_text)

    def check_password(self, password_plain_text):
        return check_password_hash(self.password_hash, password_plain_text)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
