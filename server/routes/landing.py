from flask import Blueprint
from flask_restful import Resource, Api

landing_bp = Blueprint('landing', __name__)
api = Api(landing_bp)

class Landing(Resource):
    def get(self):
        return {"message": "Welcome to the Business Management Tool"}

api.add_resource(Landing, '/')
