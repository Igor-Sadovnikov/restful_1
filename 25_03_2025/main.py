from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from . import users_resource


app = Flask(__name__)
api = Api(app)

api.add_resourse(users_resource.UsersResource, '/api/v2/users')
api.add_resorce(users_resource.UsersListResource, '/api/v2/users/<int:user_id>')