from typing import Optional, Dict

from pydantic import BaseModel


class Advertisement(BaseModel):
    advertised_price: Optional[float]
    advertisement_group_id: Optional[str]
    published_date: Optional[str]
    links: Optional[Dict]
