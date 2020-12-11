import http.server
import os
import socketserver

import punq
from requests import request

from src.data.models.transform.event_to_request import event_to_web_request
from src.handlers.web_handler import WebHandler

PORT = 8080
container = None


def set_dependency(container):
    container.register(WebHandler, WebHandler, template_prefix="C:/Work/Private/Private/BazarApp-server/")
    return container


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        global container
        print(self.path)
        if not container:
            container = punq.Container()
            container = set_dependency(container)
        handler: WebHandler = container.resolve(WebHandler)

        # print(str(_list("./", [])))
        self.send_response(200)
        self.end_headers()
        event = {'resource': '',
                 'body-json': {},
                 'params': {'path': {'controller': 'store-items', 'view': None}, 'querystring': {}, 'header': {}},
                 'stage-variables': {}, 'httpMethod': 'GET'}

        event_css = {'body-json': {},
                     'params': {'path': {'file_name': 'uploadifive.css'}, 'querystring': {}, 'header': {}},
                     'stage-variables': {},
                     'resource': '/css/{file_name}',
                     'httpMethod': 'GET',
                     'context': {'account-id': '056695529414', 'api-id': 'qasi12d9c2', 'api-key': 'test-invoke-api-key',
                                 'authorizer-principal-id': '', 'caller': '056695529414',
                                 'cognito-authentication-provider': '', 'cognito-authentication-type': '',
                                 'cognito-identity-id': '', 'cognito-identity-pool-id': '', 'http-method': 'GET',
                                 'stage': 'test-invoke-stage', 'source-ip': 'test-invoke-source-ip',
                                 'user': '056695529414',
                                 'user-agent': 'aws-internal/3 aws-sdk-java/1.11.864 Linux/4.9.217-0.3.ac.206.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.262-b10 java/1.8.0_262 vendor/Oracle_Corporation',
                                 'user-arn': 'arn:aws:iam::056695529414:root',
                                 'request-id': '4cafc6d1-ab0a-4e94-8321-bac2311b756e', 'resource-id': '87w64o',
                                 'resource-path': '/css/{file_name}'}}

        event_update = {'resource': '',
                        'body-json': {},
                        'params': {'path': {'controller': 'store-items', 'view': 'form'},
                                   'querystring': {"store_item_id": "887e85a8-0888-4325-bec9-4d6fee23b70b"},
                                   'header': {}},
                        'stage-variables': {}, 'httpMethod': 'GET'}
        event_post = {
            "body-json": {"name": "Dummy name", "longName": "test", "originalPrice": "111", "purchasePrice": "10",
                          "categorySex": "not-applicable", "categoryType": "clothes",
                          "id": "16f26ba6-4ac8-4981-819d-60502ca47f43"},
            "params": {
                "path": {
                    "controller": "store-items"
                    , "view": "form"
                }
                , "querystring": {
                }
                , "header": {
                }
            },
            "stage-variables": {
            },
            "httpMethod": "POST"
        }

        event_post_update = {
            "body-json": {"name": "Čepice a šátek", "originalPrice": "134.0", "categorySex": "not-applicable",
                          "categoryType": "clothes", "brand": "Thibo",
                          "size": {"min": "249", "max": "249", "typeSize": "by_height"},
                          "id": "887e85a8-0888-4325-bec9-4d6fee23b70b"}
            ,
            "params": {
                "path": {
                    "controller": "store-items"
                    , "view": "form"
                }
                , "querystring": {"store_item_id": "887e85a8-0888-4325-bec9-4d6fee23b70b"}
                , "header": {
                }
            },
            "stage-variables": {
            },
            "httpMethod": "PUT"
        }
        event_preserve_link = {'body-json': {},
                               'params': {'path': {}, 'querystring': {'file_name': 'test', 'mime': 'png'},
                                          'header': {}}, 'stage-variables': {},
                               'resource': '/file/presigned_upload_link', 'httpMethod': 'GET',
                               'context': {'account-id': '056695529414', 'api-id': 'qasi12d9c2',
                                           'api-key': 'test-invoke-api-key', 'authorizer-principal-id': '',
                                           'caller': '056695529414', 'cognito-authentication-provider': '',
                                           'cognito-authentication-type': '', 'cognito-identity-id': '',
                                           'cognito-identity-pool-id': '', 'http-method': 'GET',
                                           'stage': 'test-invoke-stage', 'source-ip': 'test-invoke-source-ip',
                                           'user': '056695529414',
                                           'user-agent': 'aws-internal/3 aws-sdk-java/1.11.864 Linux/4.9.217-0.3.ac.206.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.262-b10 java/1.8.0_262 vendor/Oracle_Corporation',
                                           'user-arn': 'arn:aws:iam::056695529414:root',
                                           'request-id': '84083862-b156-4708-8b34-3b2ca5130da0',
                                           'resource-id': '0q30ez', 'resource-path': '/file/presigned_upload_link'}}
        if "css" in self.path:
            response = handler.handle(event_css, None)
        else:
            response = (handler.handle(event_update , None))
        print("test")
        print(response)

        self.wfile.write(str(response["body"]).encode())


Handler = SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
