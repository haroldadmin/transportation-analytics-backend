from flask_restplus import fields, Model


def add_models_to_namespace(namespace):
    namespace.models[user_model.name] = user_model
    namespace.models[user_register_request_model.name] = user_register_request_model
    namespace.models[user_login_request_model.name] = user_login_request_model


user_model = Model("Represents a user on our system", {
    "name": fields.String(description="Name of the user"),
    "email": fields.String(description="Email of the user")
})

user_register_request_model = Model("Represents the model of the request to register a user on the service", {
    "name": fields.String(description="Name of the user", required=True),
    "email": fields.String(description="Email of the user", required=True),
    "password": fields.String(description="Password of the user", required=True)
})

user_login_request_model = Model("Represents the model of the request to login a user on the service", {
    "email": fields.String(description="Email of the user", required=True),
    "password": fields.String(description="Password of the user", required=True)
})
