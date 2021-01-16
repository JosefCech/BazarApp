from src.data.models.business.page import Page
from src.data.models.business.store_item import StoreItemDocument
from src.data.repo.base_dynamo_repo import BaseDynamoRepo


class StoreItemRepo(BaseDynamoRepo):
    def __init__(self, store_item_table):
        self._store_item_table = store_item_table

    def get_by_id(self, id):
        return self.get_from_table_by_id(self._store_item_table, id, StoreItemDocument)

    def upsert_item(self, dict):
        self.upsert_item_to_table(self._store_item_table, dict)

    def get_all_by(self, cursor=None, limit=20):
        kwargs = {"Limit": limit}
        if cursor:
            kwargs["ExclusiveStartKey"] = self._decode_last_evaluted_key(cursor)

        response = self._store_item_table.scan(**kwargs)
        items = [StoreItemDocument(**item) for item in response.get("Items")]
        return Page(
            next_link=self._encode_last_evaluted_key(response.get("LastEvaluatedKey")),
            items=items
        )


