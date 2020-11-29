from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel

from src.data.models.business.advertisement import Advertisement
from src.data.models.business.sold_item import SoldItem


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


class ClothesSizeEnum(StrEnum):
    BY_HEIGHT = 'by_height'
    BY_AGE = 'by_age'
    BY_WEIGHT = 'by_weight'


class ClothesSize(BaseModel):
    min: Optional[int]
    max: Optional[int]
    type_size: ClothesSizeEnum


class StoreItemDocument(BaseModel):
    id: str
    name: str
    long_name: Optional[str]
    description: Optional[str]
    original_price: Optional[int]
    purchase_price: Optional[int]
    sold_info: Optional[SoldItem]
    category_sex: Optional[CategorySex]
    category_type: Optional[CategoryType]
    category_subtype: Optional[str]
    brand: Optional[str]
    size: Optional[ClothesSize]
    sold_info: Optional[SoldItem]
    advertisement_info: Optional[Advertisement]
    create_at: str
    last_update_at: str
    # TODO add references to foto


class ClothesSizeByHeight(ClothesSize):
    pass


class ClothesSizeByAge(ClothesSize):
    pass


class ClothesSizeByWeight(ClothesSize):
    pass


class StoreClothesDocument(StoreItemDocument):
    size: Optional[ClothesSize]
    season: SeasonEnum = SeasonEnum.UNDEFINED


def create_dummy_store_item_document():
    return StoreItemDocument(
        id=str(uuid4()),
        name="whatever",
        long_name="long whatever",
        advertisement_info=Advertisement(advertised_price=12.50),
        sold_info=SoldItem(givenPrice=11.50),
        create_at=str(datetime.utcnow()),
        last_update_at=str(datetime.utcnow())

    )
