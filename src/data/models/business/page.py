from typing import List, TypeVar, Callable, Type, Optional

from pydantic import BaseModel

T = TypeVar('T')


class Page(BaseModel):
    items: List
    next_link: Optional[str]

    @property
    def count(self):
        return len(self.items)


def transform_page(page: Page, transform_func: Callable, target: Type):
    return Page(next_link=page.next_link, items=[transform_func(item, target) for item in page.items])
