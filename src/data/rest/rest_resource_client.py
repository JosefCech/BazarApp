from typing import Callable

import requests
from pydantic import BaseModel

from src.data.models.business.page import Page


class RestResourceClient:
    def __init__(self, base_url: str, result_trans: Callable):
        self._base_url = base_url
        self._result_trans = result_trans

    def post(self, endpoint: str, request: BaseModel, headers: dict = {}):
        url = self._get_url(endpoint)
        response = requests.post(url=url, data=request.json(), headers=headers)
        return response

    def get(self, endpoint: str, params: dict = {}, headers: dict = {}):
        url = self._get_url(endpoint)
        print(url)
        response = requests.get(url=url, headers=headers)
        print(response)
        if self._result_trans == str:
            return Page(items=response.json()["items"],
                        next_link=response.json()["next_link"])
        else:
            return Page(items=[self._result_trans(**item) for item in response.json()["items"]],
                        next_link=response.json()["next_link"])

    def get_by_id(self, endpoint: str, params: dict = {}, headers: dict = {}):
        url = self._get_url(endpoint)
        response = requests.get(url=url, headers=headers)
        response_json = response.json()
        # TODO hadle not found
        return self._result_trans(**response_json)

    def _get_url(self, endpoint):
        return f"{self._base_url}/{endpoint}"
