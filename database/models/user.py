from database import db


class UserModel(db.Model):
    __tablename__ = "users"

    def __init__(self, name, bio=""):
        self.name = name
        self.bio = bio

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    requests = db.relationship("RouteRequestModel", backref="user", lazy=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

