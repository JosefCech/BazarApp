from datetime import datetime

from src.data.models.business.advertisement_resource import AdvertisementResource, AdvertisementRequest


def advertisement_request_to_resource(request: AdvertisementRequest):
    kwargs = request.dict()
    kwargs["createAt"] = str(datetime.now())
    return AdvertisementResource(**kwargs)

