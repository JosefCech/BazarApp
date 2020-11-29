from typing import Optional, Dict
from uuid import uuid4

from pydantic import BaseModel

from src.data.models.business.store_item import CategorySex, CategoryType, ClothesSize, ClothesSizeEnum


class SoldItemRequest(BaseModel):
    soldDate: Optional[str]
    postage: Optional[float]
    givenPrice: Optional[float]


class AdvertisementRequest(BaseModel):
    advertisedPrice: Optional[float]
    description: Optional[str]
    advertisementGroupId: Optional[str]
    requestedPrice: Optional[float]
    publishedDate: Optional[str]
    links: Optional[Dict]


class ClothesSizeRequest(BaseModel):
    min: Optional[int]
    max: Optional[int]
    typeSize: ClothesSizeEnum


class StoreItemResourceRequest(BaseModel):
    id: str
    name: str
    longName: Optional[str]
    originalPrice: Optional[float]
    purchasePrice: Optional[float]
    categorySex: Optional[CategorySex]
    categoryType: Optional[CategoryType]
    categorySubtype: Optional[str]
    brand: Optional[str]
    size: Optional[ClothesSizeRequest]
    advertisementInfo: Optional[AdvertisementRequest]
    soldInfo: Optional[SoldItemRequest]
    createAt: Optional[str]


class StoreItemResourceResponse(StoreItemResourceRequest):
    lastUpdateAt: str


class StoreItemRequest(BaseModel):
    id: str
    name: str
    longName: Optional[str]
    originalPrice: Optional[float]
    purchasePrice: Optional[float]
    categorySex: CategorySex = CategorySex.NA
    categoryType: CategoryType = CategoryType.OTHER
    categorySubtype: Optional[str]
    brand: Optional[str]
    createAt: Optional[str]


class StoreItemAdvertisementRequest(StoreItemRequest):
    advertisementInfo: Optional[AdvertisementRequest]


class StoreItemAdvertisementRequest(StoreItemResourceRequest):
    soldInfo: Optional[SoldItemRequest]


def create_dummy_store_item_simple():
    return StoreItemResourceRequest(
        id=str(uuid4()),
        name="whatever",
        longName="long whatever"
    )


def create_dummy_store_item_simple():
    return StoreItemResourceRequest(
        id=str(uuid4()),
        name="whatever",
        longName="long whatever",
        advertisementInfo=AdvertisementRequest(advertised_price=12.50)
    )


def create_dummy_store_item_advertised():
    return StoreItemResourceRequest(
        id=str(uuid4()),
        name="whatever",
        longName="long whatever",
        advertisementInfo=AdvertisementRequest(advertisedPrice=12.50)
    )


def create_dummy_store_item_sold():
    return StoreItemResourceRequest(
        id=str(uuid4()),
        name="whatever",
        longName="long whatever",
        advertisementInfo=AdvertisementRequest(advertisedPrice=12.50),
        soldInfo=SoldItemRequest(givenPrice=11.50)
    )
