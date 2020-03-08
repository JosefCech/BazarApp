from datetime import datetime
from enum import Enum
from typing import Optional, List
from uuid import uuid4

from pydantic import BaseModel


class StrEnum(str, Enum):
    pass


class StoreItemStatus(Enum):
    CREATED = 'created'

    PUBLISHED = 'published'
    RESERVED = 'reserved'
    SOLD = 'sold'
    SWAPPED = 'swapped'


class StoreItemState(BaseModel):
    status: str
    start_at: str


class CategorySex(StrEnum):
    BOY = "boy"
    GIRL = 'girl'
    BOTH = "unisex"
    WOMEN = 'women'
    NA = 'not-applicable'


class CategoryType(StrEnum):
    CLOTHES = 'clothes'
    SHOES = 'shoes'
    OTHER = 'other'


class SeasonEnum(StrEnum):
    WINTER = 'winter'
    SUMMER = 'summer'
    ALL = 'whole-year'
    UNDEFINED = 'undefined'


class StoreItemRequest(BaseModel):
    id: str
    name: str
    categorySex: CategorySex = CategorySex.NA
    categoryType: CategoryType = CategoryType.OTHER
    categorySubtype: str = 'undefined'
    brand: str = 'undefined'
    season: SeasonEnum = SeasonEnum.UNDEFINED
    size: str = 'undefined'
    originalPrice: float
    boughtPrice: float


class StoreItemResource(StoreItemRequest):
    createdAt : str


class AdvertisementRequest(StoreItemRequest):
    description: Optional[str]
    publishedDate: Optional[str]
    soldDate: Optional[str]
    postage: float = 0
    advertisedPrice: float
    givenPrice: float = 0


class AdvertisementResource(AdvertisementRequest):
    createAt: str
    items: Optional[list]


class DynamoDBResponse(BaseModel):
    next_url: Optional[str]
    count: int = 0


class Advertisements(DynamoDBResponse):
    items: list


class AdvertisementsMetrics(BaseModel):
    sumGivenPrice: float
    sumOriginalPrice: float
    sumBoughtPrice: float
    returnValueRatio: float  # bought -> given
    lossValueRatio: float  # original -> given


class AdvertisementsAnalyticsResponse(BaseModel):
    totalCount: int
    usedForCalculation: int
    totalSumGivenPrice: float
    metricsOnSubset: Optional[AdvertisementsMetrics]
    metricsOnTotal: AdvertisementsMetrics


def create_dummy_advertisement_request():
    return AdvertisementRequest(
        id=str(uuid4()),
        name="whatever",
        originalPrice=10.2,
        boughtPrice=9,
        advertisedPrice=11.3
    )


def create_dummy_advertisement_resource():
    return AdvertisementResource(
        id=str(uuid4()),
        name="whatever",
        originalPrice=10.2,
        boughtPrice=9,
        advertisedPrice=4.3,
        createAt=str(datetime.now()),
    )
