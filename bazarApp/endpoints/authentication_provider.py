from flask_httpauth import HTTPBasicAuth
from jwt import PyJWT

auth = HTTPBasicAuth()

_encoded = None


class AuthenticationProvider:

    @auth.verify_password
    def verify_password(username, password=None):
        global _encoded
        print(username)
        print(password)
        if _encoded == username:
            return True
        elif (username == 'josef'):
            _encoded = str(PyJWT().encode({'name': username, 'pass': password}, 'secret', algorithm='HS256'))
            # TODO implement proper auth
            # _encoded = str(PyJWT().encode({'name': username, 'pass': password}, 'secret', algorithm='HS256'))
            print(_encoded)
            return True;

        return False


    @staticmethod
    def getToken():
        global _encoded
        return _encoded
