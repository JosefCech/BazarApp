import json
from io import open
from uuid import uuid4

from bazarApp.data.item import Item


class ItemRepo:
    def insert(self, items: Item):
        raise NotImplementedError

    def get(self, id: uuid4):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError


class FileItemRepo(ItemRepo):
    def __init__(self, file_name: str):
        self._filename = "./data/" + str(file_name)
        self._cache = {}
        self._refresh_cash()

    def upsert(self, item: Item):
        fileappend = open(self._filename, "a+")
        try:
            self._cache[item.id] = item
            fileappend.writelines(item.json() + "\n")
        finally:
            fileappend.close()

    def get(self, id: uuid4):
        if id not in self._cache.keys():
            self._refresh_cash()
        if id in self._cache.keys():
            return self._cache[id]
        else:
            return None

    def _refresh_cash(self):
        try:
            file_open = open(self._filename, "r")
            for line in file_open:
                item_json = json.loads(line)
                self._cache[item_json["id"]] = Item(**item_json)
        except FileNotFoundError as e:
            self._cache = {}


    def get_all(self):
        if not self._cache:
            self._refresh_cash()

        return self._cache.values()
