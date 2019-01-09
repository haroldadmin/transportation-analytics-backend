from flask_restplus import fields, Model


def add_models_to_namespace(namespace):
    namespace.models[route_request_model.name] = route_request_model


route_request_model = Model("Represents a Route Request", {
    "id": fields.Integer(description="Unique identifier for the ride"),
    "start_point_lat": fields.Float(description="Represents the latitude of the starting point"),
    "start_point_long": fields.Float(description="Represents the longitude of the starting point"),
    "end_point_lat": fields.Float(description="Represents the latitude of the ending point"),
    "end_point_long": fields.Float(description="Represents the longitude of the ending point")
})
