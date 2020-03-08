from flask_jwt_extended import (jwt_required)
# reactor
from flask_restplus import Resource

from src.config.pre_app import db, app
from src.data.abstract_models.user import User

USER_DATA = {
    "masnun": "abc123"
}


def verify(username, password):
    if not (username and password):
        return False
    if USER_DATA.get(username) == password:
        return User(id=123)


def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}


print(app.config['JWT_AUTH_URL_RULE'])


# @api.errorhandler(NoAuthorizationError)
# def handle_auth_error(e):
#     return {'message': str(e)}, 401


class PrivateResource(Resource):

    @jwt_required
    def get(self):
        return {"meaning_of_life": 42}


# jwt._set_error_handler_callbacks(api)
# api.add_resource(PrivateResource, '/private')
# api.add_resource(StoreItemHandler, '/add_item')


if __name__ == '__main__':
    import src.handlers.advertisement_handler
    import src.handlers.user_handler
    import src.handlers.web.main_web_handler
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8080)


