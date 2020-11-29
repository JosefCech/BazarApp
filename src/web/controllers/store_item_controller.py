from typing import List

from mako.template import Template
from pydantic import BaseModel

from src.data.models.business.store_item import CategorySex, CategoryType, SeasonEnum, ClothesSizeEnum
from src.data.models.business.store_item_resource import StoreItemResourceResponse, StoreItemResourceRequest, \
    AdvertisementRequest, SoldItemRequest, ClothesSizeRequest
from src.data.rest.rest_resource_client import RestResourceClient
from src.web.controllers.base_controller import BaseController


class StoreItemResponseWrapper(StoreItemResourceResponse):

    @property
    def is_sold(self):
        return self._is_empty_object("soldInfo", SoldItemRequest)

    @property
    def is_advertised(self):
        return self._is_empty_object("advertisementInfo", AdvertisementRequest)

    @property
    def have_size(self):
        return self._is_empty_object("size", ClothesSizeRequest)

    def _is_empty_object(self, field_name, field_type):
        is_object_empty = getattr(self, field_name) is None
        if not is_object_empty:
            objectInfo = getattr(self, field_name)
            is_params_empty = True
            for x in field_type.__fields__:
                is_params_empty = is_params_empty and getattr(objectInfo, x) is None
            is_object_empty = is_params_empty
        return not is_object_empty


class StoreItemController(BaseController):
    def __init__(self, template_prefix="./"):
        self._rest_client = RestResourceClient("https://jgfnvpor2j.execute-api.eu-west-1.amazonaws.com/v0",
                                               StoreItemResourceResponse)
        self._endpoint = "store-items"
        self._request = StoreItemResourceRequest
        super().__init__(template_prefix, "storeItems")
        self._config = {"url_api": "https://jgfnvpor2j.execute-api.eu-west-1.amazonaws.com/v0"}

    def GET_list(self, **kwargs):
        myTemplate = Template(filename=self._template_prefix + f"src/templates/{self._get_view('list')}.html")
        page = self._rest_client.get(self._endpoint)
        kwargs["items"] = [StoreItemResponseWrapper(**x.dict()) for x in page.items]
        return myTemplate.render(**kwargs)

    def GET_form(self, store_item_id=None, **kwargs):
        myTemplate = Template(filename=self._template_prefix + f"src/templates/{self._get_view('form')}.html")
        # TODO load id item
        if store_item_id:
            store_item_response = self._rest_client.get_by_id(f"/store-items/{store_item_id}")
            kwargs["update_object"] = store_item_response.dict()
            kwargs["update_object"]["is_sold"] = self._is_sold(store_item_response)
            kwargs["update_object"]["is_advertised"] = self._is_advertised(store_item_response)
            kwargs["update_object"]["have_size"] = self._have_size(store_item_response)
            print(store_item_response)

        kwargs['fields_data'] = self._get_fields_data()
        kwargs['fields'] = [key for key in StoreItemResourceRequest.__dict__["__fields__"].keys() if key != 'id']
        for x in kwargs['fields']:
            if x not in kwargs["fields_data"]:
                print(x)

        return myTemplate.render(**kwargs)

    def POST_form(self, request_object, **kwargs):
        result = self._rest_client.post("/store-items", request_object)
        response = result.json()
        if result.status_code == 200:
            response["success"] = True
        return response

    def PUT_form(self, request_object, **kwargs):
        result = self._rest_client.post(f"/store-items/{request_object.id}", request_object)
        response = result.json()
        if result.status_code == 200:
            response["success"] = True
        return response

    def _is_sold(self, store_item_response: StoreItemResourceResponse):
        return self._is_full_empty(store_item_response, "soldInfo", SoldItemRequest)

    def _is_advertised(self, store_item_response: StoreItemResourceResponse):
        return self._is_full_empty(store_item_response, "advertisementInfo", AdvertisementRequest)

    def _have_size(self, store_item_response: StoreItemResourceResponse):
        return self._is_full_empty(store_item_response, "size", ClothesSizeRequest)

    def _is_full_empty(self, store_item_response: StoreItemResourceResponse, name, info_object: BaseModel):
        is_object_empty = getattr(store_item_response, name) is None
        if not is_object_empty:
            objectInfo = getattr(store_item_response, name)
            is_params_empty = True
            for x in info_object.__fields__:
                is_params_empty = is_params_empty and getattr(objectInfo, x) is None
            is_object_empty = is_params_empty

        return not is_object_empty

    def _get_fields_data(self):
        fields_data = {
            "categorySex": {"type": "select",
                            "values": [item.value for item in CategorySex],
                            "default": "not-applicable"},
            "categoryType": {"type": "select",
                             "values": [item.value for item in CategoryType],
                             "default": "others"},
            "season": {"type": "select",
                       "values": [item for item in SeasonEnum],
                       "default": "undefined"},
            "description": {"type": "textarea"},
            "longName": {"type": "textarea"},
            "name": {"type": "text", "required": True},

            "originalPrice": {"hidden": False,
                              "type": "price",
                              "default": "0"
                              },
            "purchasePrice": {"hidden": False,
                              "type": "price",
                              "default": "0"
                              },
            "brand": {"type": "text"},
            "categorySubtype": {"type": "text"},

            "soldInfo": {"hidden": False,
                         "type": "inner",
                         "check_value": "is_sold",
                         "inner_field_list": [key for key in
                                              SoldItemRequest.__dict__["__fields__"].keys() if
                                              key != 'id'],
                         },
            "advertisementInfo": {"hidden": False,
                                  "type": "inner",
                                  "check_value": "is_advertised",
                                  "inner_field_list": [key for key in
                                                       AdvertisementRequest.__dict__["__fields__"].keys() if
                                                       key != 'id'],
                                  },

            "createAt": {"hidden": True, "type": "text"},
            "advertisementGroupId": {
                "hidden": True,
                "type": "text"
            },
            "links": {
                "hidden": True,
                "type": "text"
            },
            "publishedDate": {
                "type": "date",
                "default": "DD-MM-YYYY"
            },
            "advertisedPrice": {
                "type": "price",
                "default": "0"
            },
            "soldDate": {
                "type": "date",
                "default": "DD-MM-YYYY"
            },
            "postage": {
                "default": 0,
                "type": "price",
            },
            "givenPrice": {
                "default": 0,
                "type": "price",
            },
            "requestedPrice": {
                "type": "price"
            },
            "size": {
                "hidden": False,
                "type": "inner",
                "check_value": "have_size",
                "inner_field_list": [key for key in
                                     ClothesSizeRequest.__dict__["__fields__"].keys() if
                                     key != 'id'],
            },
            "min": {
                "type": "number"
            },
            "max": {
                "type": "number"
            },
            "typeSize": {"type": "select",
                         "values": [item.value for item in ClothesSizeEnum],
                         "default": "others"}

        }
        return fields_data

    def _get_data(self, **kwargs) -> List[StoreItemResourceResponse]:
        raise NotImplementedError

    def _get_by_id(self, id):
        raise NotImplementedError
