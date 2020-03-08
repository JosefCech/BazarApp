from flask import render_template

from src.config.pre_app import app


class MainWebHandler:
    @staticmethod
    @app.route('/index', endpoint="/index", methods=['GET'])
    def handle():
        print("Test")
        return render_template('index.html')