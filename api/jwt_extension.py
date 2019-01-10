from flask_jwt_extended import JWTManager

from api import api

jwt = JWTManager()

jwt._set_error_handler_callbacks(api)

@jwt.expired_token_loader
def my_expired_token_callback():
    return {
               'message': 'The token has expired! Please, login again.'
           }, 401


# The error_message argument is necessary so that the message can be redirected to the user
# If it is not present, the flask app will raise and Error when a request with invalid auth header is made
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
