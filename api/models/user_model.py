from flask_restplus import fields, Model

user_model = Model("Represents a user on our system", {
    "name": fields.String(description="Name of the user"),
    "email": fields.String(description="Email of the user")
})