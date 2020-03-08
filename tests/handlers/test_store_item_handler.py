from unittest.mock import MagicMock

import punq

from src.data.models.business.advertisement_resource import create_dummy_advertisement_resource, \
    create_dummy_advertisement_request
from src.handlers.advertisement_handler import AdvertisementHandler
from src.server import set_dependency


def test_get_endpoint_succesfull():
    container = punq.Container()
    set_dependency(container, MagicMock())
    handler = container.resolve(AdvertisementHandler)
    handler._advertisement_repo.get_by_id = MagicMock()
    handler._advertisement_repo.get_by_id.return_value = create_dummy_advertisement_resource()
    response = handler.get_advertisement("test")
    assert response.get("statusCode") == 200
    assert "create" in response.get("body")


def test_get_endpoint_not_found():
    container = punq.Container()
    set_dependency(container, MagicMock())
    handler = container.resolve(AdvertisementHandler)
    handler._advertisement_repo.get_by_id = MagicMock()
    handler._advertisement_repo.get_by_id.return_value = None
    response = handler.get_advertisement("test")
    assert response.get("statusCode") == 404


def test_post_endpoint():
    container = punq.Container()
    set_dependency(container, MagicMock())
    handler = container.resolve(AdvertisementHandler)
    handler._advertisement_repo.get_by_id = MagicMock()
    handler._advertisement_repo.get_by_id.return_value = None
    response = handler.upsert_item(create_dummy_advertisement_request())
    assert response.get("statusCode") == 201


def test_post_endpoin_failed_save():
    container = punq.Container()
    set_dependency(container, MagicMock())
    handler = container.resolve(AdvertisementHandler)
    handler._advertisement_repo.get_by_id = MagicMock()
    handler._advertisement_repo.get_by_id.return_value = None
    handler._advertisement_repo.upsert_item = MagicMock()
    handler._advertisement_repo.upsert_item.side_effect = Exception("Saved to dynamodb fails")
    response = handler.upsert_item(create_dummy_advertisement_request())
    assert response.get("statusCode") == 500
    assert "Saved to dynamodb fails" in response.get('body')

def test_post_endpoint_already_exists():
    container = punq.Container()
    set_dependency(container, MagicMock())
    handler = container.resolve(AdvertisementHandler)
    handler._advertisement_repo.get_by_id = MagicMock()
    handler._advertisement_repo.get_by_id.return_value = create_dummy_advertisement_resource()
    response = handler.upsert_item(create_dummy_advertisement_request())
    assert response.get("statusCode") == 400