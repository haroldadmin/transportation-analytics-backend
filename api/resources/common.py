from flask_restplus import reqparse

# This is for documentation purposes in Swagger only
auth_header_parser = reqparse.RequestParser()
auth_header_parser.add_argument('Authorization',
                                required=True,
                                help='Authentication access token. E.g.: Bearer <access_token>',
                                location='headers')
