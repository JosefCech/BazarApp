import os

from mako import exceptions
from mako.template import Template
from punq import Container

from src.config import config
from src.data.models.business.request import WebRequest, Response
from src.data.models.business.store_item_resource import StoreItemResourceRequest
from src.data.models.transform.event_to_request import event_to_web_request
from src.handlers.base_handler import endpoint, BaseHandler
from src.localization.cz.advertisement import lang
from src.web.controllers.file_controller import FileController
from src.web.controllers.store_item_controller import StoreItemController


def _list(basepath, result):
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            # print(basepath)
            _list(os.path.join(basepath, entry), result)
        if os.path.isfile(os.path.join(basepath, entry)):
            #  print(os.path.join(basepath, entry))
            result.append(os.path.join(basepath, entry))
    return result


class WebHandler(BaseHandler):
    def __init__(self, template_prefix="./"):
        super().__init__(request_transformation=event_to_web_request)
        self._template_prefix = template_prefix
        self._container = Container()
        self._container.register("StoreItemsController", StoreItemController, template_prefix=template_prefix)
        self._config = config

    def common_handle(self, request: WebRequest):
        controller_name = self._snake_to_camel_case(request.path["controller"]) + 'Controller'
        view = f"{request.method}_{request.path.get('view')}" if request.path.get("view") else "GET_list"
        kwargs = {"lang": lang, "base_api_path": "https://qasi12d9c2.execute-api.eu-west-1.amazonaws.com/v0/web",
                  "base_web_path": "https://qasi12d9c2.execute-api.eu-west-1.amazonaws.com/v0/web"}

        if request.method in ["PUT", "POST"]:
            request_object = StoreItemResourceRequest(**request.body)
            kwargs["request_object"] = request_object

        kwargs = {**request.parameters, **kwargs}

        controller = self._container.resolve(controller_name)
        try:
            response = getattr(controller, view)(**kwargs)
        except Exception:
            error = exceptions.html_error_template().render()
            # print(error)
            return self.make_html_response(error.decode('utf-8'))

        if request.method == "GET":
            return self.make_html_response(response)
        else:
            return self.make_response(content=response, status_code=200)

    # return self.make_response(template, status_code=200, headers=None)

    @endpoint("/css/{file_name}", methods=["GET"])
    def handle_css(self, file_name: str):

        with open(f'{self._template_prefix}/src/web/css/{file_name}', 'r') as reader:
            return self.make_html_response(reader.read())

    @endpoint("/js/{file_name}", methods=["GET"])
    def handle_js(self, file_name: str):

        with open(f'{self._template_prefix}/src/web/js/{file_name}', 'r') as reader:
            return self.make_html_response(reader.read())

    @endpoint("/img/{store_item_id}/{file_name}", methods=["GET"])
    def handle_img(self, store_item_id: str, file_name: str):
        return {
             'headers': {'Location': f'https://{config["ImageS3Bucket"]}.s3.amazonaws.com/{store_item_id}/{file_name}'},
             'statusCode': 302,
             'body': f'https://{config["ImageS3Bucket"]}.s3.amazonaws.com/{store_item_id}/{file_name}',
             'isBase64Encoded': False
        }



        # return {
        #     'headers': {"Content-Type": "image/png"},
        #     'statusCode': 200,
        #     'body': base64.b64encode(image_bytes),
        #     'isBase64Encoded': True
        # }

        # return self.make_raw_response(content=base64.b64encode(image_bytes), headers={"Content-Type": ["image/jpeg"]})

    @endpoint("/web", methods=["GET"])
    def index(self):
        myTemplate = Template(filename=self._template_prefix + "src/templates/index.html")
        dir_content = _list("./", [])
        # print(str(dir_content))
        # return self.make_html_response(str(dir_content))
        return self.make_html_response(myTemplate.render(fields=[], fields_data=self._get_fields_data(), lang=lang))

    @endpoint("/file/presigned_upload_link/{file_name}", methods=["GET"])
    def preserve_link(self, file_name):
        controller = FileController()
        return self.make_response(
            content=controller.presigned_upload(bucket_name=self._config.get("ImageS3Bucket"), object_name=file_name),
            status_code=200)

    def _snake_to_camel_case(self, controller_name):
        if controller_name.find('_') != -1 or controller_name.find('-') != -1:
            camel_name = ''.join([w.capitalize() for w in controller_name.split('_')])
            camel_name2 = ''.join([w.capitalize() for w in camel_name.split('-')])
            return camel_name2
        return controller_name
