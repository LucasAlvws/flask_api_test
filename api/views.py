from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from resources.user import UserList, UserResource

blueprint = Blueprint("api", __name__, url_prefix="/api/")

api =  Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(UserList, "/users/")
api.add_resource(UserResource, "/users/<int:id>/")

@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400
