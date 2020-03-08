from src.data.models.business.advertisement_resource import AdvertisementResource, Advertisements
from src.data.repo.base_repo import BaseRepo


class AdvertisementRepo(BaseRepo):
    def __init__(self, advertisement_table: str):
        self._advertisement_table = advertisement_table

    def get_by_id(self, id):
        return self.get_from_table_by_id(self._advertisement_table, id, AdvertisementResource)

    def upsert_item(self, dict):
        self.upsert_item_to_table(self._advertisement_table, dict)

    def get_all_by(self, cursor=None, limit=20) -> Advertisements:
        kwargs = {"Limit": limit}
        if cursor:
            kwargs["ExclusiveStartKey"] = self._decode_last_evaluted_key(cursor)

        response = self._advertisement_table.scan(**kwargs)
        items = [AdvertisementResource(**item) for item in response.get("Items")]
        return Advertisements(
            next_url=self._encode_last_evaluted_key(response.get("LastEvaluatedKey")),
            count=len(items),
            items=items
        )
