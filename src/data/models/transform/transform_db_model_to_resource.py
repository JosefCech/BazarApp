from datetime import datetime

from pydantic import BaseModel

from src.data.models.business.advertisement import Advertisement
from src.data.models.business.sold_item import SoldItem
from src.data.models.business.store_item import ClothesSize
from src.data.models.business.store_item_resource import AdvertisementRequest, SoldItemRequest, ClothesSizeRequest


def _snake_to_camel_case(field_name: str):
    if field_name.find('_') != -1:
        camel_name = ''.join([w.capitalize() for w in field_name.split('_')])
        return camel_name[0].lower() + camel_name[1:]
    return field_name


def transform_resquest_to_business_model(request_instance: BaseModel, model_type):
    SUBMODELS_TO_DOC = {
        AdvertisementRequest: Advertisement,
        SoldItemRequest: SoldItem,
        ClothesSizeRequest: ClothesSize
    }

    data = {x: request_instance.__getattribute__(_snake_to_camel_case(x)) for x in
            model_type.__dict__['__fields__'].keys() if hasattr(request_instance, _snake_to_camel_case(x))}

    for x in [m for m in data if isinstance(data[m], BaseModel)]:
        data[x] = transform_resquest_to_business_model(data[x], SUBMODELS_TO_DOC[type(data[x])])
    if not data.get("create_at"):
        data["create_at"] = str(datetime.utcnow())
    data["last_update_at"] = str(datetime.utcnow())
    return model_type(**data)


def transform_business_model_response(model_instance: BaseModel, response_type):
    DOC_TO_SUBMODELS = {
        Advertisement: AdvertisementRequest,
        SoldItem: SoldItemRequest,
        ClothesSize : ClothesSizeRequest
    }
    data = {_snake_to_camel_case(x): model_instance.__getattribute__(x) for x in
            type(model_instance).__dict__['__fields__'].keys()}

    for x in [m for m in data if isinstance(data[m], BaseModel)]:
        data[x] = transform_business_model_response(data[x], DOC_TO_SUBMODELS[type(data[x])])

    return response_type(**data)
