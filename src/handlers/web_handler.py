from mako.template import Template

from src.data.models.business.advertisement_resource import AdvertisementRequest, CategorySex, CategoryType, SeasonEnum, \
    StoreItemRequest
from src.handlers.base_handler import endpoint, BaseHandler
from src.localization.cz.advertisement import lang


class WebHandler(BaseHandler):
    def __init__(self, template_prefix="./"):
        super().__init__()
        self._template_prefix = template_prefix

    @endpoint("/web", methods=["GET"])
    def index(self):
        myTemplate = Template(filename=self._template_prefix + "src/templates/index.html")
        return self.make_response(myTemplate, status_code=200, headers=None)

    @endpoint("/web/advertisement-form", methods=["GET"])
    def advertisement_form(self):
        myTemplate = Template(filename=self._template_prefix + "src/templates/advertisement-form.html")
        fields = [key for key in AdvertisementRequest.__dict__["__fields__"].keys() if key != 'id']
        return self.make_html_response(myTemplate.render(fields=fields, fields_data=self._get_fields_data(), lang=lang))

    @endpoint("/web/store-item-form", methods=["POST"])
    def store_item_form(self):
        myTemplate = Template(filename=self._template_prefix + "src/templates/storeItem-form.html")
        fields = [key for key in StoreItemRequest.__dict__["__fields__"].keys() if key != 'id']
        return self.make_html_response(myTemplate.render(fields=fields, fields_data=self._get_fields_data(), lang=lang))

    def _get_fields_data(self):
        fields_data = {
            "categorySex": {"type": "select",
                            "values": [item for item in CategorySex],
                            "default": "not-applicable"},
            "categoryType": {"type": "select",
                             "values": [item for item in CategoryType],
                             "default": "others"},
            "season": {"type": "select",
                       "values": [item for item in SeasonEnum],
                       "default": "undefined"},
            "description": {"type": "textarea"},
            "publishedDate": {"type": "date",
                              "default": "DD/MM/YYYY"},
            "soldDate": {"type": "date",
                         "default": "DD/MM/YYYY",
                         "hidden": True
                         },
            "postage": {"hidden": True,
                        "default": "0"
                        },
            "givenPrice": {"hidden": True,
                           "default": "0"}

        }
        return fields_data