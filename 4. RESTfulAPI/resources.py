from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required
from models import db, UserModel, ItemModel

class RegisterUser(Resource):
    def post(self):
        data = request.get_json()
        if UserModel.query.filter_by(username=data['username']).first():
            return {'message': 'User already registered'}, 400

        user = UserModel(username=data['username'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User successfully created'}, 201

class LoginUser(Resource):
    def post(self):
        data = request.get_json()
        user = UserModel.query.filter_by(username=data['username']).first()

        if user and user.verify_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return {'token': access_token}, 200

        return {'message': 'Invalid credentials'}, 401

class ItemDetail(Resource):
    @jwt_required()
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return {'id': item.id, 'name': item.name, 'description': item.description}

    @jwt_required()
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {'message': 'Item removed'}

    @jwt_required()
    def put(self, item_id):
        data = request.get_json()
        item = ItemModel.query.get_or_404(item_id)
        item.name = data['name']
        item.description = data['description']
        db.session.commit()
        return {'id': item.id, 'name': item.name, 'description': item.description}

class ItemList(Resource):
    @jwt_required()
    def get(self):
        items = ItemModel.query.all()
        return [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]

    @jwt_required()
    def post(self):
        data = request.get_json()
        item = ItemModel(name=data['name'], description=data['description'])
        db.session.add(item)
        db.session.commit()
        return {'id': item.id, 'name': item.name, 'description': item.description}, 201
