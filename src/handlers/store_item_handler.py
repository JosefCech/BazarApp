from logging import Logger

from src.analytics.advertisements_analytics import AdvertisementsAnalytics
from src.data.models.business.advertisement_resource import AdvertisementRequest, StoreItemRequest
from src.data.models.transform.advertisement_transformation import advertisement_request_to_resource
from src.data.models.transform.store_item_transformation import store_item_request_to_resource
from src.data.repo.advertisement_repo import AdvertisementRepo
from src.data.repo.store_item_repo import StoreItemRepo
from src.handlers.base_handler import endpoint, BaseHandler

logger = Logger("store_item")


class StoreItemHandler(BaseHandler):
    def __init__(self, store_item_repo: StoreItemRepo):
        super().__init__()
        self._store_item_repo = store_item_repo

    @endpoint("/store-item/{id}", methods=["GET"])
    def get_store_item(self, id: str):
        resource = self._store_item_repo.get_by_id(id)
        if not resource:
            logger.warning(f"Item {id} not founc")
            return self.make_response("{}", 404)
        return self.make_response(resource, 200)

    @endpoint("/store-item", methods=["GET"])
    def get_store_items(self):
        resource = self._store_item_repo.get_all_by()
        if not resource:
            logger.warning(f"Item {id} not found")
            return self.make_response("{}", 404)
        return self.make_response(resource, 200)

    @endpoint("/store-item", methods=["POST"])
    def upsert_item(self, item_request: StoreItemRequest):
        existing_item = self._store_item_repo.get_by_id(item_request.id)
        if existing_item:
            return self.make_response('{message :"Item with' + item_request.id + ' already exists"}', 400)
        resource = store_item_request_to_resource(item_request)
        try:
            self._store_item_repo.upsert_item(resource.dict())
        except Exception as e:
            return self.make_response('{message :"' + str(e) + '"}', 500)
        return self.make_response(resource, 201)
