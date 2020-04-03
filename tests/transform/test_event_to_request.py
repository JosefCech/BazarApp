from src.data.models.transform.event_to_request import event_to_request

get_simple_event ={'resource': '/lambda', 'path': '/lambda', 'httpMethod': 'GET',
             'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'cs-CZ,cs;q=0.9',
                         'cache-control': 'no-cache', 'CloudFront-Forwarded-Proto': 'https',
                         'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false',
                         'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false',
                         'CloudFront-Viewer-Country': 'CZ', 'content-type': 'application/json',
                         'Host': 'e29fsbt0p9.execute-api.eu-west-1.amazonaws.com',
                         'postman-token': '86ca0fca-f130-aa99-3250-54b70fbd9dbe', 'sec-fetch-mode': 'cors',
                         'sec-fetch-site': 'cross-site',
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                         'Via': '2.0 0f538ee832e1105649039b38ce89e883.cloudfront.net (CloudFront)',
                         'X-Amz-Cf-Id': 'YwJh9HHdTVToZdT5d6XrCyfL8J3BT5Ej7G_CILWs_Mv0VpwbWvRjQw==',
                         'X-Amzn-Trace-Id': 'Root=1-5e46fe79-6dcd87400b91b5188db75248',
                         'X-Forwarded-For': '217.30.64.210, 70.132.63.144', 'X-Forwarded-Port': '443',
                         'X-Forwarded-Proto': 'https'},
             'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate, br'],
                                   'Accept-Language': ['cs-CZ,cs;q=0.9'], 'cache-control': ['no-cache'],
                                   'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'],
                                   'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'],
                                   'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-Country': ['CZ'],
                                   'content-type': ['application/json'],
                                   'Host': ['e29fsbt0p9.execute-api.eu-west-1.amazonaws.com'],
                                   'postman-token': ['86ca0fca-f130-aa99-3250-54b70fbd9dbe'],
                                   'sec-fetch-mode': ['cors'], 'sec-fetch-site': ['cross-site'], 'User-Agent': [
                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'],
                                   'Via': ['2.0 0f538ee832e1105649039b38ce89e883.cloudfront.net (CloudFront)'],
                                   'X-Amz-Cf-Id': ['YwJh9HHdTVToZdT5d6XrCyfL8J3BT5Ej7G_CILWs_Mv0VpwbWvRjQw=='],
                                   'X-Amzn-Trace-Id': ['Root=1-5e46fe79-6dcd87400b91b5188db75248'],
                                   'X-Forwarded-For': ['217.30.64.210, 70.132.63.144'], 'X-Forwarded-Port': ['443'],
                                   'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None,
             'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None,
             'requestContext': {'resourceId': 'xw7l5g', 'resourcePath': '/lambda', 'operationName': 'lambda',
                                'httpMethod': 'GET', 'extendedRequestId': 'H5yy7Ft5joEFkkg=',
                                'requestTime': '14/Feb/2020:20:09:29 +0000', 'path': '/v0/lambda',
                                'accountId': '056695529414', 'protocol': 'HTTP/1.1', 'stage': 'v0',
                                'domainPrefix': 'e29fsbt0p9', 'requestTimeEpoch': 1581710969066,
                                'requestId': '33c0e129-8c37-48c5-80f2-3dcf2d02f3d8',
                                'identity': {'cognitoIdentityPoolId': None, 'accountId': None,
                                             'cognitoIdentityId': None, 'caller': None, 'sourceIp': '217.30.64.210',
                                             'principalOrgId': None, 'accessKey': None,
                                             'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None,
                                             'userArn': None,
                                             'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                                             'user': None},
                                'domainName': 'e29fsbt0p9.execute-api.eu-west-1.amazonaws.com', 'apiId': 'e29fsbt0p9'},
             'body': None, 'isBase64Encoded': False}


def test_event_to_request():
    request = event_to_request(get_simple_event)
    assert request.method == 'GET'
    assert request.endpoint == '/lambda'