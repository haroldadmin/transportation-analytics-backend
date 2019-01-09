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


@ns.route("/<int:req_id")
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
