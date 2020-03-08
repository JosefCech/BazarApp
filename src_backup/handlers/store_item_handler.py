import logging

from flask import jsonify, Response, request
from flask_jwt_extended import jwt_required

from src.config.pre_app import db, app
from src.data.abstract_models.store_item_resource import StoreItemResource
from src.data.db_models.store_item_model import StoreItemModel
from src.data.transform.transform_db_model_to_resource import transform_resource_to_model, transform_model_to_resource
from src.handlers.base_handler import convert_json_input_to, convert_parameters_input_to_dict

logger = logging.getLogger()


class StoreItemHandler():
    # @app.route('/')
    # @app.route('/index')
    # def get():
    #     db.create_all()
    #     db.session.add(store_item_resource.create_dummy_store_item_model())
    #     db.session.commit()
    #     return store_item_resource.create_dummy_store_item_resource().json()

    @app.route('/store_item', methods=['POST','PUT'])
    @convert_json_input_to(class_=StoreItemResource)
    def upsert(self, data: StoreItemResource):
        logger.info(f"Save item with id {data.id} ")
        if request.method == "POST":
            if StoreItemModel.query.filter_by(id=data.id):
                logger.warning(f"Object with id {data.id} already exists")
                return Response('{"message" : "No item with id ' + data.id + '"}', status=400)

            db.session.add(transform_resource_to_model(data, StoreItemModel))
            db.session.commit()
            logger.info(f"Success! Item with id {data.id} was saved ")
            return Response(jsonify(data.dict()), status=201)
        else:
            if StoreItemModel.query.filter_by(id=data.id):
                db.session.merge(transform_resource_to_model(data, StoreItemModel))
                db.session.commit()
                logger.info(f"Success! Item with id {data.id} was saved ")
                return jsonify(data.dict())
            logger.warning(f"Object with id {data.id} nor exists")
            return Response('{"message" : "No item with id ' + data.id + '"}', status=400)


    @app.route('/store_item/<store_item_id>', methods=['GET'])
    def get(store_item_id: str):
        logger.info(f"Load item with {store_item_id} ")
        return jsonify(transform_model_to_resource(StoreItemModel.query.filter_by(id=store_item_id).first(),
                                                   StoreItemResource).dict())

    @app.route('/search', endpoint="/search", methods=['GET'])
    @convert_parameters_input_to_dict()
    @jwt_required
    def search(self, get_params):
        logger.info(f"Start search with {get_params} ")
        for x in get_params:
            if not x in ['item_type', 'item_subtype', 'season', 'name']:
                raise ValueError(f"not allowed search {x}")
        data = StoreItemModel.query.filter_by(**get_params)
        logger.info(f"End search with params {get_params} ")
        return jsonify({'_items': [transform_model_to_resource(x, StoreItemResource).dict() for x in data]})
