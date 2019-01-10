from flask_jwt_extended import JWTManager
from flask_restplus import Api
from api.resources.users import ns as users_namespace
from api.resources.requests import ns as requests_namespace

api = Api(
    title="Tranportation Analytics Platform",
    version="0.1",
    description="A platform generating analytics about a city's transportation sytem"
)

api.add_namespace(users_namespace, path="/users")
api.add_namespace(requests_namespace, path="/requests")

jwt = JWTManager()

jwt._set_error_handler_callbacks(api)

@jwt.expired_token_loader
def my_expired_token_callback():
    return {
               'message': 'The token has expired! Please, login again.'
           }, 401


@jwt.invalid_token_loader
def my_invalid_token_callback(error_message):
    return {
               'message': 'The token is invalid!'
           }, 401


@jwt.unauthorized_loader
def my_unauthorized_request_callback(error_message):
    return {
               'message': 'The authorization token is missing!'
           }, 401