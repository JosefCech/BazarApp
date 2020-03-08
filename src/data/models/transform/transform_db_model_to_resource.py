from flask_sqlalchemy import Model
from pydantic import BaseModel


def transform_resource_to_model(resource: BaseModel, model):
    resource_data = vars(resource)
    return model(**resource_data)


def transform_model_to_resource(model: Model, resource):
    if model :
        model_data = {x: model.__getattribute__(x) for x in resource.__dict__['__fields__'].keys()}
        return resource(**model_data)
    else:
        return {}
