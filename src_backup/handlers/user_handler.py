from flask import jsonify
from flask_jwt_extended import create_access_token

from src.config.pre_app import app


class UserHandler:
    @app.route('/auth', endpoint="/auth", methods=['GET'])
    def authorize():
        token = create_access_token("josef")
        return jsonify({'token': token})
