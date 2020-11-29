from mako.template import Template

from src.data.models.business.advertisement_resource import CategorySex, CategoryType, SeasonEnum
from src.web.controllers.base_controller import BaseController


class AdvertisementController(BaseController):
    def __init__(self, template_prefix="./"):
        super().__init__(template_prefix, "advertisement")


    def form(self):
        pass

    def list(self, **kwargs):
        myTemplate = Template(filename=self._template_prefix + f"src/templates/{self._get_view('list')}.html")
        return myTemplate.render(**kwargs)

    def form(self, **kwargs):
        myTemplate = Template(filename=self._template_prefix + f"src/templates/{self._get_view('form')}.html")
        return myTemplate.render(**kwargs)

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


