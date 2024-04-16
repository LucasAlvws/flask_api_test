from http import HTTPStatus

from flask_restful import Resource, abort
from flask import request
from flask.json import jsonify

from serializers.users import UserSerializer
from models.users import User
from extensions import db


class UserList(Resource):
    def get(self):
        users = User.query.all()
        serializer = UserSerializer(many=True)
        return {"results": serializer.dump(users)}

    def post(self):
        serializer = UserSerializer()
        validated_data = serializer.load(request.json)
        user = User(**validated_data)
        db.session.add(user)
        db.session.commit()
        return {
            "msg": "User created",
            "user": serializer.dump(user),
        }, HTTPStatus.CREATED


class UserResource(Resource):

    def get(self, id):
        user = User.query.get_or_404(id)
        serializer = UserSerializer()
        return {"user": serializer.dump(user)}

    def put(self, id):
        serializer = UserSerializer(partial=True)
        user = User.query.get_or_404(id)
        user = serializer.load(request.json, instance=user)
        db.session.add(user)
        db.session.commit()
        return {"msg": "User updated.", "user": serializer.dump(user)}

    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"msg":"User has been delete."}, HTTPStatus.NO_CONTENT
