import os

import boto3
import punq

from src.analytics.advertisements_analytics import AdvertisementsAnalytics
from src.analytics.advertisements_calculation import AdvertisementsCalculation
from src.config import config
from src.data.repo.advertisement_repo import AdvertisementRepo
from src.data.repo.file_repo import FileRepo
from src.data.repo.store_item_repo import StoreItemRepo
from src.handlers.advertisement_handler import AdvertisementHandler
from src.handlers.store_item_handler import StoreItemHandler


def handle(event, context):
    response = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'multiValueHeaders': {},
        'body': f'{str(event)}'
    }
    return response


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
    container.register(FileRepo, FileRepo, bucket_name=config["ImageS3Bucket"])
    container.register(AdvertisementHandler, AdvertisementHandler)
    container.register(StoreItemHandler, StoreItemHandler)
    return container


def handle_crud(event, context):
    global container
    if not container:
        container = punq.Container()
        container = set_dependency(container)
    handler = container.resolve(StoreItemHandler)
    return handler.handle(event, context)
