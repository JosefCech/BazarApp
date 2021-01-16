from logging import Logger

from src.data.models.business.page import transform_page
from src.data.models.business.store_item import StoreItemDocument
from src.data.models.business.store_item_resource import StoreItemResourceResponse, StoreItemResourceRequest, \
    StoreItemPhotos
from src.data.models.transform.transform_db_model_to_resource import transform_business_model_response, \
    transform_resquest_to_business_model
from src.data.repo.file_repo import FileRepo
from src.data.repo.store_item_repo import StoreItemRepo
from src.handlers.base_handler import endpoint, BaseHandler

logger = Logger("store_item")


class StoreItemHandler(BaseHandler):
    def __init__(self, store_item_repo: StoreItemRepo, file_repo: FileRepo):
        super().__init__()
        self._store_item_repo = store_item_repo
        self._image_repo = file_repo

    @endpoint("/store-items/{id}", methods=["GET"])
    def get_store_item(self, id: str):
        resource = self._store_item_repo.get_by_id(id)
        if not resource:
            logger.warning(f"Item {id} not found")
            return self.make_response("{}", 404)
        response = transform_business_model_response(resource, StoreItemResourceResponse)
        return self.make_response(response, 200)

    @endpoint("/store-items/{id}", methods=["POST"])
    def update_item(self, id: str, item_request: StoreItemResourceRequest):
        if id != item_request.id:
            return self.make_response({"message": f"Ids doesn't match"}, 409)
        resource = transform_resquest_to_business_model(item_request, StoreItemDocument)
        try:
            self._store_item_repo.upsert_item(resource.dict())
        except Exception as e:
            return self.make_response('{message :"' + str(e) + '"}', 500)
        response = transform_business_model_response(resource, StoreItemResourceResponse)
        return self.make_response(response, 200)

    @endpoint("/store-items", methods=["GET"])
    def get_store_items(self):
        resource = self._store_item_repo.get_all_by()
        if not resource:
            logger.warning(f"Nothing not found")
            return self.make_response("{}", 404)
        try:
            print(resource)
            return self.make_response(
                transform_page(resource, transform_business_model_response, StoreItemResourceResponse), 200)
        except:
            print(resource)

    @endpoint("/store-items", methods=["POST"])
    def create_item(self, item_request: StoreItemResourceRequest):
        existing_item = self._store_item_repo.get_by_id(item_request.id)
        if existing_item:
            return self.make_response({"message": f"Item with {item_request.id} already exists"}, 400)
        resource: StoreItemDocument = transform_resquest_to_business_model(item_request, StoreItemDocument)
        try:
            self._store_item_repo.upsert_item(resource.dict())
        except Exception as e:
            return self.make_response('{message :"' + str(e) + '"}', 500)
        response = transform_business_model_response(resource, StoreItemResourceResponse)
        return self.make_response(response, 201)

    @endpoint("/store-items/{id}/{subitem}", methods=["GET"])
    def get_store_items_subitem(self, id, subitem):
        if "photo" in subitem:
            keys = self._image_repo.list_s3_keys(prefix=id)
            return self.make_response(StoreItemPhotos(items=keys, next_link=""), 200)
        else:
            return self.make_response({"error": f"subitem {subitem} not supported"}, status_code=400)
