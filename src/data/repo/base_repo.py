import json
from base64 import urlsafe_b64encode, urlsafe_b64decode
from decimal import Decimal
from typing import Callable


class BaseRepo():


    def _encode_last_evaluted_key(self, last_evaluated_key):
        if last_evaluated_key:
            return urlsafe_b64encode(bytes(str(last_evaluated_key), "utf-8"))
        else :
            return None

    def _decode_last_evaluted_key(self, cursor):
        if cursor:
            cursor_bytes = urlsafe_b64decode(cursor)
            cursor_str = cursor_bytes.decode('utf-8')
            json_acceptable_string = cursor_str.replace("'", "\"")
            return json.loads(json_acceptable_string)
        else:
            return None

    def get_from_table_by_id(self, table, id, transformation : Callable):
        item_document = table.get_item(Key={"id": id})
        if not item_document.get('Item'):
            return None
        return transformation(**item_document.get('Item'))

    def upsert_item_to_table(self, table, dict):
        dynamo_object = json.loads(json.dumps(dict), parse_float=Decimal)
        table.put_item(Item=dynamo_object)
