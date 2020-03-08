from logging import Logger

from src.analytics.advertisements_analytics import AdvertisementsAnalytics
from src.data.models.business.advertisement_resource import AdvertisementRequest
from src.data.models.transform.advertisement_transformation import advertisement_request_to_resource
from src.data.repo.advertisement_repo import AdvertisementRepo
from src.handlers.base_handler import endpoint, BaseHandler

logger = Logger("store_item")


class AdvertisementHandler(BaseHandler):
    def __init__(self, advertisement_repo: AdvertisementRepo, advertisement_analytics: AdvertisementsAnalytics):
        super().__init__()
        self._advertisement_repo = advertisement_repo
        self._advertitsements_analytics = advertisement_analytics

    @endpoint("/advertisement/{id}", methods=["GET"])
    def get_advertisement(self, id: str):
        resource = self._advertisement_repo.get_by_id(id)
        if not resource:
            logger.warning(f"Item {id} not founc")
            return self.make_response("{}", 404)
        return self.make_response(resource, 200)

    @endpoint("/advertisement", methods=["GET"])
    def get_advertisements(self):
        resource = self._advertisement_repo.get_all_by()
        if not resource:
            logger.warning(f"Item {id} not found")
            return self.make_response("{}", 404)
        return self.make_response(resource, 200)

    @endpoint("/advertisement/analytics", methods=["GET"])
    def get_advertisements_analytics(self):
        resource = self._advertisement_repo.get_all_by()
        if not resource:
            logger.warning(f"No items found")
            return self.make_response("{}", 404)

        analytics = self._advertitsements_analytics.create_analytics(resource.items)
        return self.make_response(analytics, 200)

    @endpoint("/advertisement", methods=["POST"])
    def upsert_item(self, item_request: AdvertisementRequest):
        existing_item = self._advertisement_repo.get_by_id(item_request.id)
        if existing_item:
            return self.make_response('{message :"Item with' + item_request.id + ' already exists"}', 400)
        resource = advertisement_request_to_resource(item_request)
        try:
            self._advertisement_repo.upsert_item(resource.dict())
        except Exception as e:
            return self.make_response('{message :"' + str(e) + '"}', 500)
        return self.make_response(resource, 201)
