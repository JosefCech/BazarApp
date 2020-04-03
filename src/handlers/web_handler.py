from mako.template import Template
from punq import Container

from src.data.models.business.advertisement_resource import AdvertisementRequest, CategorySex, CategoryType, SeasonEnum, \
    StoreItemRequest
from src.data.models.transform.event_to_request import event_to_web_request
from src.handlers.base_handler import endpoint, BaseHandler
from src.localization.cz.advertisement import lang
from src.web.controllers.advertisement import AdvertisementController


class WebHandler(BaseHandler):
    def __init__(self, template_prefix="./"):
        super().__init__()
        self._template_prefix = template_prefix
        self._container = Container()
        self._container.register(AdvertisementController, AdvertisementController)


    def handle(self, event, context):
        request = event_to_web_request(event)
        controller_name = request.path["controller"] + 'Controller'
        view = request.path["view"] if request.path["view"] else "base_view"
        method =

        controller = self._container.resolve(controller_name)
        kwargs = {}
        template = getattr(controller, view)(**kwargs)

        return self.make_response(template, status_code=200, headers=None)





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