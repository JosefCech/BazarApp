from typing import List, Dict, Optional, NamedTuple, Union

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
    body: Union[str, bytes]
    statusCode: int
    headers: Dict[str, List[str]] = None



class WebRequest(NamedTuple):
    endpoint: str
    path: Optional[dict]
    method: str
    parameters: Optional[dict]
    body: Optional[dict]
    headers: Optional[dict]
    event: dict

    def key(self):
        return f'{self.endpoint}-{self.method}'
