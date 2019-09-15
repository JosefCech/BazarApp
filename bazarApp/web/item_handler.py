from flask import make_response, render_template, Blueprint

from app import container
from bazarApp.config import Config
from bazarApp.data.item_repo import FileItemRepo
from bazarApp.endpoints.authentication_provider import auth, AuthenticationProvider

blueprintH = Blueprint('items', __name__)
items_repo = container.resolve(FileItemRepo)


class ItemHandler:
    def __init__(self):
        self.items_repo = FileItemRepo(Config.file_repo)

    @blueprintH.route('/items')
    @auth.login_required
    def get_all():
        all = items_repo.get_all()
        return make_response(
            render_template('items.html', items=all)
        )

    @blueprintH.route('/items/<id>')
    @auth.login_required
    def get_item(id):
        item = items_repo.get(id)
        return make_response(
            render_template('item.html', item=item)
        )


