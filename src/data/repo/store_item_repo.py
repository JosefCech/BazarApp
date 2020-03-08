from src.data.models.business.advertisement_resource import StoreItemResource
from src.data.repo.base_repo import BaseRepo


class StoreItemRepo(BaseRepo):
    def __init__(self, store_item_repo):
        self._store_item_repo = store_item_repo

    def get_by_id(self, id):
        return self.get_from_table_by_id(self._store_item_table, id, StoreItemResource)

    def upsert_item(self, dict):
        self.upsert_item_to_table(self._store_item_table, dict)
