from database import db


class RequestModel(db.Model):
    __tablename__ = "requests"

    def __init__(self, start_point_lat, start_point_long, end_point_lat, end_point_long):
        self.start_point_lat = start_point_lat
        self.start_point_long = start_point_long
        self.end_point_lat = end_point_lat
        self.end_point_long = end_point_long

    id = db.Column(db.Integer, primary_key=True)
    start_point_lat = db.Column(db.Float, nullable=False)
    end_point_lat = db.Column(db.Float, nullable=False)
    start_point_long = db.Column(db.Float, nullable=False)
    end_point_long = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
