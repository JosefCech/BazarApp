from src.data.models.business.store_item import StoreItemDocument, create_dummy_store_item_document
from src.data.models.business.store_item_resource import create_dummy_store_item_simple, \
    create_dummy_store_item_advertised, create_dummy_store_item_sold, StoreItemResourceResponse
from src.data.models.transform.transform_db_model_to_resource import transform_resquest_to_business_model, \
    transform_business_model_response


def test_store_item_request_to_document_simple():
    item = create_dummy_store_item_simple()
    document = transform_resquest_to_business_model(item, StoreItemDocument)
    assert isinstance(document, StoreItemDocument)
    assert item.id == document.id
    assert item.name == document.name
    assert item.longName == document.long_name


def test_store_item_request_to_document_advertised():
    item = create_dummy_store_item_advertised()
    document = transform_resquest_to_business_model(item, StoreItemDocument)
    assert isinstance(document, StoreItemDocument)
    assert item.id == document.id
    assert item.name == document.name
    assert item.longName == document.long_name
    assert item.advertisementInfo.advertisedPrice
    assert item.advertisementInfo.advertisedPrice == document.advertisement_info.advertised_price


def test_store_item_request_to_document_sold():
    item = create_dummy_store_item_sold()
    document = transform_resquest_to_business_model(item, StoreItemDocument)
    assert isinstance(document, StoreItemDocument)
    assert item.id == document.id
    assert item.name == document.name
    assert item.longName == document.long_name
    assert item.advertisementInfo.advertisedPrice
    assert item.advertisementInfo.advertisedPrice == document.advertisement_info.advertised_price
    assert item.soldInfo.givenPrice
    assert item.soldInfo.givenPrice == document.sold_info.given_price


def test_store_item_document_to_response():
   #document = create_dummy_store_item_document()
    item = create_dummy_store_item_sold()
    document: StoreItemDocument = transform_resquest_to_business_model(item, StoreItemDocument)
    response = transform_business_model_response(document, StoreItemResourceResponse)
    assert isinstance(response, StoreItemResourceResponse)
    assert document.name == response.name
    assert document.id == response.id
    assert document.advertisement_info.advertised_price == response.advertisementInfo.advertisedPrice
    assert document.sold_info.given_price == response.soldInfo.givenPrice
