from time import sleep

import sqlalchemy
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql-development',
    'port': '3306',
    'database': 'testapp',
    'auth_plugin': 'mysql_native_password'
}
if False:
    success = False
    while not success:
        try:
            connection = sqlalchemy.create_engine('mysql+mysqlconnector://root:password@mysql-development:3306/testapp?auth_plugin=mysql_native_password')
        except Exception as e:
            print(e)
            sleep(5)
            success = False

#sleep(30)
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#api = Api(app, prefix="/api/v1")

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)
app.config['JWT_AUTH_URL_RULE'] = "/auth"

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@mysql-development:3306/testapp?auth_plugin=mysql_native_password'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:helloworld@localhost:3308/testapp'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://test:test1234@db/mysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
