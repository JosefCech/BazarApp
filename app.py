import punq as punq
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_login import LoginManager

from bazarApp.config import Config
from bazarApp.data.item_repo import FileItemRepo

container = punq.Container()
container.register(FileItemRepo, FileItemRepo, file_name=Config.file_repo )

from bazarApp.web.item_form import item_form_print
from bazarApp.web.item_handler import blueprintH
from bazarApp.web.loginform import bp

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app.register_blueprint(bp)
app.register_blueprint(blueprintH)
app.register_blueprint(item_form_print)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = False
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



if __name__ == "__main__":
    app.run()
