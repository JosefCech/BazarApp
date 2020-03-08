from src.handlers.base_handler import BaseHandler, Endpoint

get_simple_event = {"resource": "/lambda/{id}", "path": "/lambda", "httpMethod": "GET",
                    "headers": {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br",
                                "Accept-Language": "cs-CZ,cs;q=0.9",
                                "cache-control": "no-cache", "CloudFront-Forwarded-Proto": "https",
                                "CloudFront-Is-Desktop-Viewer": "true", "CloudFront-Is-Mobile-Viewer": "false",
                                "CloudFront-Is-SmartTV-Viewer": "false", "CloudFront-Is-Tablet-Viewer": "false",
                                "CloudFront-Viewer-Country": "CZ", "content-type": "application/json",
                                "Host": "e29fsbt0p9.execute-api.eu-west-1.amazonaws.com",
                                "postman-token": "86ca0fca-f130-aa99-3250-54b70fbd9dbe", "sec-fetch-mode": "cors",
                                "sec-fetch-site": "cross-site",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
                                "Via": "2.0 0f538ee832e1105649039b38ce89e883.cloudfront.net (CloudFront)",
                                "X-Amz-Cf-Id": "YwJh9HHdTVToZdT5d6XrCyfL8J3BT5Ej7G_CILWs_Mv0VpwbWvRjQw==",
                                "X-Amzn-Trace-Id": "Root=1-5e46fe79-6dcd87400b91b5188db75248",
                                "X-Forwarded-For": "217.30.64.210, 70.132.63.144", "X-Forwarded-Port": "443",
                                "X-Forwarded-Proto": "https"},
                    "multiValueHeaders": {"Accept": ["*/*"], "Accept-Encoding": ["gzip, deflate, br"],
                                          "Accept-Language": ["cs-CZ,cs;q=0.9"], "cache-control": ["no-cache"],
                                          "CloudFront-Forwarded-Proto": ["https"],
                                          "CloudFront-Is-Desktop-Viewer": ["true"],
                                          "CloudFront-Is-Mobile-Viewer": ["false"],
                                          "CloudFront-Is-SmartTV-Viewer": ["false"],
                                          "CloudFront-Is-Tablet-Viewer": ["false"], "CloudFront-Viewer-Country": ["CZ"],
                                          "content-type": ["application/json"],
                                          "Host": ["e29fsbt0p9.execute-api.eu-west-1.amazonaws.com"],
                                          "postman-token": ["86ca0fca-f130-aa99-3250-54b70fbd9dbe"],
                                          "sec-fetch-mode": ["cors"], "sec-fetch-site": ["cross-site"], "User-Agent": [
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"],
                                          "Via": ["2.0 0f538ee832e1105649039b38ce89e883.cloudfront.net (CloudFront)"],
                                          "X-Amz-Cf-Id": ["YwJh9HHdTVToZdT5d6XrCyfL8J3BT5Ej7G_CILWs_Mv0VpwbWvRjQw=="],
                                          "X-Amzn-Trace-Id": ["Root=1-5e46fe79-6dcd87400b91b5188db75248"],
                                          "X-Forwarded-For": ["217.30.64.210, 70.132.63.144"],
                                          "X-Forwarded-Port": ["443"],
                                          "X-Forwarded-Proto": ["https"]}, "queryStringParameters": None,
                    "multiValueQueryStringParameters": None, "pathParameters": {"id": "test"}, "stageVariables": None,
                    "requestContext": {"resourceId": "xw7l5g", "resourcePath": "/lambda", "operationName": "lambda",
                                       "httpMethod": "GET", "extendedRequestId": "H5yy7Ft5joEFkkg=",
                                       "requestTime": "14/Feb/2020:20:09:29 +0000", "path": "/v0/lambda",
                                       "accountId": "056695529414", "protocol": "HTTP/1.1", "stage": "v0",
                                       "domainPrefix": "e29fsbt0p9", "requestTimeEpoch": 1581710969066,
                                       "requestId": "33c0e129-8c37-48c5-80f2-3dcf2d02f3d8",
                                       "identity": {"cognitoIdentityPoolId": None, "accountId": None,
                                                    "cognitoIdentityId": None, "caller": None,
                                                    "sourceIp": "217.30.64.210",
                                                    "principalOrgId": None, "accessKey": None,
                                                    "cognitoAuthenticationType": None,
                                                    "cognitoAuthenticationProvider": None,
                                                    "userArn": None,
                                                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
                                                    "user": None},
                                       "domainName": "e29fsbt0p9.execute-api.eu-west-1.amazonaws.com",
                                       "apiId": "e29fsbt0p9"},
                    "body": None, "isBase64Encoded": False}

post_simple_event = {'resource': '/lambda', 'path': '/lambda', 'httpMethod': 'POST', 'headers': None,
                     'multiValueHeaders': None, 'queryStringParameters': None, 'multiValueQueryStringParameters': None,
                     'pathParameters': None, 'stageVariables': None,
                     'requestContext': {'resourceId': 'n1poa3', 'resourcePath': '/lambda', 'operationName': 'lambda',
                                        'httpMethod': 'POST', 'extendedRequestId': 'H_UXzHTDjoEFkkg=',
                                        'requestTime': '16/Feb/2020:12:23:13 +0000', 'path': '/lambda',
                                        'accountId': '056695529414', 'protocol': 'HTTP/1.1',
                                        'stage': 'test-invoke-stage', 'domainPrefix': 'testPrefix',
                                        'requestTimeEpoch': 1581855793844,
                                        'requestId': 'da8cd0a3-603d-4a4b-8851-bd545a264adc',
                                        'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None,
                                                     'apiKey': 'test-invoke-api-key', 'principalOrgId': None,
                                                     'cognitoAuthenticationType': None,
                                                     'userArn': 'arn:aws:iam::056695529414:root',
                                                     'apiKeyId': 'test-invoke-api-key-id',
                                                     'userAgent': 'aws-internal/3 aws-sdk-java/1.11.714 Linux/4.9.184-0.1.ac.235.83.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.242-b08 java/1.8.0_242 vendor/Oracle_Corporation',
                                                     'accountId': '056695529414', 'caller': '056695529414',
                                                     'sourceIp': 'test-invoke-source-ip',
                                                     'accessKey': 'ASIAQ2M2RD7DMJE4K3NB',
                                                     'cognitoAuthenticationProvider': None, 'user': '056695529414'},
                                        'domainName': 'testPrefix.testDomainName', 'apiId': 's0ut9dmul2'},
                     'body': '{   \r\n    "id": "dummy_id",\r\n    "name": "dummy_name",\r\n    "item_type": "dummy_item_type",\r\n    "item_subtype": "dummy_subtype",\r\n    "season": "season1",\r\n    "color": "color1",\r\n    "original_price": 10.25,\r\n    "requested_price": 10.25\r\n}',
                     'isBase64Encoded': False}
executed = None


def get_item(request):
    global executed
    executed = "GET"


def post_item(request):
    global executed
    executed = "POST"


endpoints = [Endpoint('/lambda/{id}', ['GET'], get_item), Endpoint('/lambda', ['POST'], post_item)]


def test_get_endpoint():
    handler = BaseHandler()
    handler.endpoints = endpoints
    global executed
    handler.handle(get_simple_event, None)
    assert executed=="GET"


def test_post_endpoint():
    handler = BaseHandler()
    handler.endpoints = endpoints
    global executed
    handler.handle(post_simple_event, None)
    assert executed == "POST"
