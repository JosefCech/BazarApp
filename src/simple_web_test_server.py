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
    container.register(WebHandler, WebHandler, template_prefix="/home/josef/Work/josef/BazarApp/")
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

        event = {'resource': '',
                 'body-json': {},
                 'params': {'path': {'controller': 'store-items', 'view': None}, 'querystring': {}, 'header': {}},
                 'stage-variables': {}, 'httpMethod': 'GET'}

        event_item = {'body-json': {}, 'params': {'path': {'controller': 'store-items', 'view': 'form'}, 'querystring': {'store_item_id': '887e85a8-0888-4325-bec9-4d6fee23b70b'}, 'header': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'cs-CZ,cs;q=0.9,en;q=0.8', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'CZ', 'Host': 'qasi12d9c2.execute-api.eu-west-1.amazonaws.com', 'Referer': 'https://qasi12d9c2.execute-api.eu-west-1.amazonaws.com/v0/web/store-items', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36', 'Via': '2.0 7df0d6b4ce8f8b155434dd5d830b76be.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'Btn5b_UY2D97MGrLqoqLZxls-87hV3UAvE0wwvrV5zuFnNYn178onA==', 'X-Amzn-Trace-Id': 'Root=1-5ff073ca-35efb7ac74510c0910115e3b', 'X-Forwarded-For': '90.179.67.223, 130.176.143.108', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}}, 'stage-variables': {}, 'httpMethod': 'GET', 'resource': '/web/{controller}/{view}'}
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

        event_js = {'body-json': {},
                     'params': {'path': {'file_name': 'uploadifive.css'}, 'querystring': {}, 'header': {}},
                     'stage-variables': {},
                     'resource': '/js/{file_name}',
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
                                 'resource-path': '/js/{file_name}'}}

        event_img = {'body-json': {},
                    'params': {'path': {'file_name': 'uploadifive.css'}, 'querystring': {}, 'header': {}},
                    'stage-variables': {},
                    'resource': '/img/{file_name}',
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
                                'resource-path': '/img/{file_name}'}}


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
            splitted_path = self.path.split('/')
            print(splitted_path)
            event_css['params']['path']['file_name'] = splitted_path[-1]
            self.send_header("Content-type", "text/css")
            response = handler.handle(event_css, None)
        elif "js" in self.path:
            splitted_path = self.path.split('/')
            print(splitted_path)
            event_js['params']['path']['file_name'] = splitted_path[-1]
            self.send_header("Content-type", "text/javascript")
            response = handler.handle(event_js, None)
        elif "img" in self.path:
            splitted_path = self.path.split('/')
            print(splitted_path)
            event_img['params']['path']['file_name'] = splitted_path[-1]
            self.send_header("Content-type", "image/jpeg")
            response = handler.handle(event_img, None)
        else:
            response = (handler.handle(event_item , None))
        print("test")
        print(response)



        if "img" not in self.path :
            self.end_headers()
            self.wfile.write(str(response["body"]).encode())
        else:
            self.send_header("Accept-Ranges", "bytes")
            self.send_response(200)
            self.send_header("Content-Length", len(response['body']))
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(response["body"])

Handler = SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
