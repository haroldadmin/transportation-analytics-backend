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