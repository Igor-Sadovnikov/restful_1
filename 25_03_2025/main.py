from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from . import users_resource
from data import db_session

app = Flask(__name__)
api = Api(app)

api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')


if __name__ == '__main__':
    db_session.global_init('base.db')
    app.run(port=8080, host='127.0.0.1')