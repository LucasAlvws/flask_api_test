from http import HTTPStatus

from flask_restful import Resource, abort
from flask import request
from flask.json import jsonify

from models.users import User
from extensions import db


class UserList(Resource):
    def get(self):
        users = User.query.all()
        return jsonify(results=users)

    def post(self):
        data = request.json
        user = User(
            name=data.get("name"),
            email=data.get("email"),
            age=data.get("age"),
        )
        db.session.add(user)
        db.session.commit()
        return jsonify(msg="User created", user=user)


class UserResource(Resource):

    def get(self, id):
        user = User.query.get_or_404(id)
        return jsonify(user = user)

    def put(self, id):
        user = User.query.get_or_404(id)
        data = request.json
        user.name = data.get("name")
        user.age = data.get("age")
        db.session.commit()
        return jsonify(msg="User updated.", user = user)

    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify(msg="User has been delete.")
