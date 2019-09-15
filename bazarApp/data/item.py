from uuid import uuid4

from pydantic import BaseModel


class Item(BaseModel):
    id: str
    name: str
    rest: dict


def dummy_item():
    return Item(id=str(uuid4()),
                name='whatever',
                rest={}
                )
