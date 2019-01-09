from flask import request
from flask_restplus import Namespace, Resource, marshal

from api.models import user_model
from api.models.user_model import add_models_to_namespace
from database.models.user import UserModel

ns = Namespace("users", description="Operations related to users")
add_models_to_namespace(ns)


@ns.route("/")
class UserCollection(Resource):

    @classmethod
    @ns.marshal_with(user_model)
    def get(cls):
        return UserModel.query.all()


@ns.route("/<int:user_id>")
@ns.param("user_id", "The ID of the requested user")
class UserProfile(Resource):

    @classmethod
    def get(cls, user_id):
        user = UserModel.query.get(user_id)
        if not user:
            return {
                       "message": "User not found"
                   }, 404

        return marshal(user, user_model), 200


@ns.route("users")
class UserRegister(Resource):

    @classmethod
    @ns.marshal_with(user_model)
    def post(cls):
        data = request.json

        name = data["name"]
        bio = data["bio"]

        user = UserModel(name, bio)
        user.save_to_db()

        return user, 200
