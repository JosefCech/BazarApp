import http.server
import os
import socketserver

import boto3
import punq

from src.analytics.advertisements_analytics import AdvertisementsAnalytics
from src.analytics.advertisements_calculation import AdvertisementsCalculation
from src.data.repo.advertisement_repo import AdvertisementRepo
from src.data.repo.store_item_repo import StoreItemRepo
from src.handlers.advertisement_handler import AdvertisementHandler
from src.handlers.store_item_handler import StoreItemHandler


PORT = 8080
container = None


def set_dependency(container, boto_session=boto3):
    dynamodb_resource = boto_session.resource('dynamodb')
    advertisement_table_name = os.getenv("AdvertisementTable", "store_items_v1")
    store_item_table_name = os.getenv("StoreItemTable", "store_items_v1")
    advertisement_name = dynamodb_resource.Table(advertisement_table_name)
    store_item_table = dynamodb_resource.Table(store_item_table_name)
    container.register(AdvertisementsCalculation, AdvertisementsCalculation)
    container.register(AdvertisementsAnalytics, AdvertisementsAnalytics)
    container.register(AdvertisementRepo, AdvertisementRepo, advertisement_table=advertisement_name)
    container.register(StoreItemRepo, StoreItemRepo, store_item_table=store_item_table)
    container.register(AdvertisementHandler, AdvertisementHandler)
    container.register(StoreItemHandler, StoreItemHandler)
    return container


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        global container
        if not container:
            container = punq.Container()
            container = set_dependency(container)
        handler = container.resolve(StoreItemHandler)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(handler.store_item_form()).encode())

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(post_body)


Handler = SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
