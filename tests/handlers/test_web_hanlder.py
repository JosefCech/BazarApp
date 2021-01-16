import punq

from src.handlers.web_handler import WebHandler

def set_dependency(container):
    container.register(WebHandler, WebHandler, template_prefix="/home/josef/Work/josef/BazarApp/")
    return container

def test_list_event():
    event = {'body-json': {}, 'body': {}, 'params': {'path': {'controller': 'StoreItems'}, 'querystring': {},
                                                     'header': {
                                                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                                         'Accept-Encoding': 'gzip, deflate, br',
                                                         'Accept-Language': 'cs-CZ,cs;q=0.9,en;q=0.8',
                                                         'cache-control': 'max-age=0',
                                                         'CloudFront-Forwarded-Proto': 'https',
                                                         'CloudFront-Is-Desktop-Viewer': 'true',
                                                         'CloudFront-Is-Mobile-Viewer': 'false',
                                                         'CloudFront-Is-SmartTV-Viewer': 'false',
                                                         'CloudFront-Is-Tablet-Viewer': 'false',
                                                         'CloudFront-Viewer-Country': 'CZ',
                                                         'Host': 'qasi12d9c2.execute-api.eu-west-1.amazonaws.com',
                                                         'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
                                                         'sec-fetch-site': 'none', 'sec-fetch-user': '?1',
                                                         'upgrade-insecure-requests': '1',
                                                         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                                                         'Via': '2.0 7cfba11baf6016eafce83142b99c8ff8.cloudfront.net (CloudFront)',
                                                         'X-Amz-Cf-Id': 'lTfjZFvphyvrK0Dmni3F_t9_a_O_G1xxegMGvAsLbOPyCCF7rfXJUQ==',
                                                         'X-Amzn-Trace-Id': 'Root=1-5ff06eb1-5f01d65124d53ff44be4f21e',
                                                         'X-Forwarded-For': '90.179.67.223, 130.176.143.142',
                                                         'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}},
             'stage-variables': {}, 'resource': '/web/{controller}', 'path': '/web/{controller}', 'httpMethod': 'GET',
             'headers': {},
             'context': {'account-id': '', 'api-id': 'qasi12d9c2', 'api-key': '', 'authorizer-principal-id': '',
                         'caller': '', 'cognito-authentication-provider': '', 'cognito-authentication-type': '',
                         'cognito-identity-id': '', 'cognito-identity-pool-id': '', 'http-method': 'GET', 'stage': 'v0',
                         'source-ip': '90.179.67.223', 'user': '',
                         'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                         'user-arn': '', 'request-id': '921a9035-ed5f-4fd3-925a-be7b877e14bd', 'resource-id': '2805i6',
                         'resource-path': '/web/{controller}'}}
    container = None
    if not container:
        container = punq.Container()
        container = set_dependency(container)
    handler: WebHandler = container.resolve(WebHandler)
    handler.handle(event, None)
