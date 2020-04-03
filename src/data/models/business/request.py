from typing import List, Dict, Optional, NamedTuple

from pydantic import BaseModel


class Request(NamedTuple):
    endpoint: str
    method: str
    parameters: Optional[Dict]
    body: Optional[Dict]
    headers: Optional[Dict]
    event: Dict

    def key(self):
        return f'{self.endpoint}-{self.method}'


class Response(BaseModel):
    body: str
    statusCode: int
    headers: Dict[str, List[str]] = None


class WebRequest:
    endpoint: str
    path: Optional[dict]
    method: str
    parameters: Optional[dict]
    body: Optional[dict]
    headers: Optional[dict]
    event: dict

    def key(self):
        return f'{self.endpoint}-{self.method}'
