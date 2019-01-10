from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restplus import Namespace, Resource, marshal

from api.models.request import add_models_to_namespace, route_request_model
from api.resources.common import auth_header_parser
from database.models.route_request import RouteRequestModel

ns = Namespace("route-requests", description="Operations related to ride requests")
add_models_to_namespace(ns)


@ns.route("/")
class RequestsCollection(Resource):

    @classmethod
    @jwt_required
    @ns.expect(auth_header_parser)
    @ns.marshal_list_with(route_request_model)
    def get(cls):
        return RouteRequestModel.query.all()


@ns.route("/<int:req_id>")
@ns.param("user_id", "The ID of the requested route request")
class RouteRequest(Resource):

    @classmethod
    @jwt_required
    @ns.expect(auth_header_parser)
    def get(cls, req_id):
        req = RouteRequestModel.query.get(req_id)

        if not req:
            return {
                       "message": "Route Request not found"
                   }, 404

        return marshal(req, route_request_model), 200


@ns.route("/")
class CreateRouteRequest(Resource):

    @classmethod
    @jwt_required
    @ns.expect(auth_header_parser)
    def post(cls):
        data = request.json

        start_point_lat = data["start_point_lat"]
        start_point_long = data["start_point_long"]
        end_point_lat = data["end_point_lat"]
        end_point_long = data["end_point_long"]
        user_id = get_jwt_identity()

        route_request = RouteRequestModel(start_point_lat,
                                          start_point_long,
                                          end_point_lat,
                                          end_point_long)

        route_request.user_id = user_id
        route_request.save_to_db()
        return marshal(route_request, route_request_model), 200
