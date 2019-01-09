from flask_restplus import fields, Model


def add_models_to_namespace(namespace):
    namespace.models[user_model.name] = user_model


user_model = Model("Represents a user on our system", {
    "name": fields.String(description="Name of the user"),
    "email": fields.String(description="Email of the user")
})
