from flask import Blueprint, request
from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token
from models.users import User
from database import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
api = Api(auth_bp)

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        role = data.get("role")

        if User.query.filter_by(username=username).first():
            return {"message": "User already exists"}, 400

        user = User(username=username, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return {"message": "Invalid credentials"}, 401

        token = create_access_token(identity={"id": user.id, "role": user.role})
        return {"token": token, "user": user.to_dict()}, 200

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
