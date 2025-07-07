from flask import Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required, get_jwt_identity

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')
api = Api(dashboard_bp)

class Dashboard(Resource):
    @jwt_required()
    def get(self):
        user = get_jwt_identity()
        return {"message": f"Welcome {user['role']} to your dashboard"}

api.add_resource(Dashboard, '/')
