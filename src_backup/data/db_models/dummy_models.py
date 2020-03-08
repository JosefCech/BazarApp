from src.data.abstract_models.store_item_resource import create_dummy_store_item_resource
from src.data.db_models.store_item_model import StoreItemModel
from src.data.transform.transform_db_model_to_resource import transform_resource_to_model


def create_dummy_store_item_model():
    return transform_resource_to_model(create_dummy_store_item_resource(), StoreItemModel)