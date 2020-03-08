from datetime import datetime

from src.data.models.business.advertisement_resource import AdvertisementResource, StoreItemRequest


def store_item_request_to_resource(request: StoreItemRequest):
    kwargs = request.dict()
    kwargs["createAt"] = str(datetime.now())
    return AdvertisementResource(**kwargs)
