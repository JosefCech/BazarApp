from src.data.models.business.advertisement_resource import create_dummy_advertisement_request
from src.data.models.transform.advertisement_transformation import advertisement_request_to_resource


def test_store_item_request_to_resource():
    request = create_dummy_advertisement_request()
    resource = advertisement_request_to_resource(request)
    assert resource