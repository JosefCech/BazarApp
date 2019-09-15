from uuid import uuid4

from flask import request, flash, render_template, Blueprint, make_response, redirect, url_for
from flask_login import current_user
from wtforms import Form, StringField, validators

from bazarApp.data.item import Item
from bazarApp.data.item_repo import FileItemRepo
from bazarApp.endpoints.authentication_provider import AuthenticationProvider

bp = Blueprint('auth', __name__, url_prefix='/')


class ReusableForm(Form):
    name = StringField('Name:', validators=[validators.required()])

    @bp.route("/", methods=['GET'])
    def hello():
        form = ReusableForm(request.form)

        print(form.errors)
        if request.method == 'POST':
            name = request.form['name']
            repo = FileItemRepo("test")
            item = Item(id=str(uuid4()), data=name, rest={})
            repo.insert(item)

            if form.validate():
                # Save the comment here.
                flash('Hello ' + name)
            else:
                flash('All the form fields are required. ')
        return make_response(render_template('form.html', form=form), 200)

    @bp.route("/", methods=['POST'])
    def login_from():
        print('Logged')
        if AuthenticationProvider.verify_password( request.form['name']):
            print('Authenticated')
            return redirect(url_for('items.get_all'))
        else:
            print('Not authenticated')
        return make_response(render_template('form.html', form=form), 200)


