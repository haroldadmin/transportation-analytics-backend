from flask import request
from flask_restplus import Namespace, Resource, marshal

from api.models.request import add_models_to_namespace, route_request_model
from database.models.route_request import RouteRequestModel

ns = Namespace("route-requests", description="Operations related to ride requests")
add_models_to_namespace(ns)


@ns.route("/")
class RequestsCollection(Resource):

    @classmethod
    def get(cls):
        return RouteRequestModel.query.all()


@ns.route("/<int:req_id>")
@ns.param("user_id", "The ID of the requested route request")
class RouteRequest(Resource):

    @classmethod
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
    def post(cls):
        data = request.json

        start_point_lat = data["start_point_lat"]
        start_point_long = data["start_point_long"]
        end_point_lat = data["end_point_lat"]
        end_point_long = data["end_point_long"]
        user_id = 1

        route_request = RouteRequestModel(start_point_lat,
                                          start_point_long,
                                          end_point_lat,
                                          end_point_long)

        route_request.user_id = user_id
        route_request.save_to_db()
        return marshal(route_request, route_request_model), 200
