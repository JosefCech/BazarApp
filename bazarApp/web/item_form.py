import datetime
import os
from uuid import uuid4

from flask import request, render_template, Blueprint, make_response, url_for
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileAllowed
from werkzeug.utils import secure_filename, redirect
from wtforms import Form, StringField, validators, TextAreaField, MultipleFileField, DateTimeField

from bazarApp.data.item import Item
from bazarApp.web.item_handler import items_repo

item_form_print = Blueprint('item_form', __name__, url_prefix='/')

photos_types = UploadSet('photos', IMAGES)


class ItemForm(Form):
    name = StringField('Name:', validators=[validators.required()])
    short_description = TextAreaField('ShortDescription')
    description = TextAreaField('Description')
    quantity = StringField('Quantity')
    actual_cost = StringField('ActualCost')
    cost = StringField('Cost')
    revenue = StringField('Revenue')

    facebook_link = StringField("FacebookLink")
    bluehorse_link = StringField("BlueHorseLink")
    vinted_link = StringField("VintedLink")
    reserved = StringField("Reserved")

    photos = MultipleFileField('Images',
                               validators=[FileAllowed(photos_types, u'Image only!'), FileAllowed(u'File was empty!')])

    @item_form_print.route("/items/new", methods=['GET'])
    def item_new():
        form = ItemForm(request.form)
        return make_response(render_template('update_form.html', form=form), 200)

    @item_form_print.route("/items/update/<id>", methods=['GET'])
    def update_new(id):
        form = ItemForm(request.form)
        item = items_repo.get(id)
        form.name.data = item.name
        form.short_description.data = item.rest.get('short_description') if not None else ''
        form.description.data = item.rest.get('description')
        form.quantity.data = item.rest.get('quantity') if not None else 0
        form.cost.data = item.rest.get('cost') if not None else 0
        form.revenue.data = item.rest.get('revenue') if not None else 0
        form.actual_cost.data = item.rest.get('actual_cost') if not None else 0
        form.facebook_link.data = item.rest.get('facebook_link')
        form.bluehorse_link.data = item.rest.get('bluehorse_link')
        form.vinted_link.data = item.rest.get('vinted_link')
        form.reserved.data = item.rest.get('reserved')

        return make_response(render_template('update_form.html', form=form, updated_item=item), 200)

    @item_form_print.route("/items/update/<id>", methods=['POST'])
    def save_item_2(id):
        form = ItemForm(request.form)
        if form.validate():
            files = request.files.getlist('photos')
            item = items_repo.get(id)
            update_item = get_item(form=form, id=id, files=files, photos=item.rest.get('photos'), item=item)
            items_repo.upsert(update_item)
            return redirect(url_for('items.get_all'))
        else:
            return make_response("Validation error", 400)

    @item_form_print.route("/items/new", methods=['POST'])
    def save_item():
        form = ItemForm(request.form)
        files = request.files.getlist('photos')
        if form.validate():
            item = get_item(form=form, files=files)
            items_repo.upsert(item)
            return redirect(url_for('items.get_all'))
        else:
            return make_response("Validation error", 400)


def get_item(form, id=None, files=None, photos=[], item=None):
    name = form['name'].data
    description = form['description'].data
    quantity = form['quantity'].data
    cost = form['cost'].data
    short_description = form['short_description'].data
    revenue = form['revenue'].data
    facebook_link = form['facebook_link'].data
    bluehorse_link = form['bluehorse_link'].data
    vinted_link = form['vinted_link'].data
    reserved = form['reserved'].data
    actual_cost = form['actual_cost'].data

    if item is None :
        published_date = datetime.datetime.now()
        sold_date = None
    else:
        published_date = item.rest.get('published_data')
        sold_date = item.rest.get("sold_date")

    if not published_date:
        published_date = datetime.datetime.now()

    if photos is None:
        photos = []
    if form.validate():
        # Save the comment here.
        photos_names_list = []
        for photo in files:
            data_filename = secure_filename(photo.filename)
            if data_filename is not None and data_filename != '':
                photo.save(os.path.join("static/images", data_filename))
                photos_names_list.append(data_filename)

        return Item(id=id if id is not None else str(uuid4()), name=name, rest={'short_descripiton': short_description,
                                                                                'description': description,
                                                                                'photos': photos_names_list + photos,
                                                                                'quantity': quantity,
                                                                                'cost': cost,
                                                                                'revenue': revenue,
                                                                                'facebook_link': facebook_link,
                                                                                'bluehorse_link': bluehorse_link,
                                                                                'vinted_link': vinted_link,
                                                                                'reserved': reserved,
                                                                                'sold_date' : sold_date,
                                                                                'published_date' : published_date,
                                                                                'actual_cost' : actual_cost
                                                                                })
