from typing import Optional

from pydantic import BaseModel


class SoldItem(BaseModel):
    gift: bool = False
    sold_date: Optional[str]
    postage: Optional[float] = 0
    given_price: Optional[float] = 0
