from src.data.models.business.request import Request, WebRequest


def event_to_request(event):
    endpoint = event['resource']
    method = event['httpMethod']
    parameters = event.get('queryStringParameters')
    parameters = {} if not parameters else parameters
    multiple_parameters = event.get('multiValueQueryStringParameters')
    multiple_parameters = {} if not multiple_parameters else multiple_parameters
    path_parameters = event.get('pathParameters')
    path_parameters = {} if not path_parameters else path_parameters
    parameters = {**parameters, **multiple_parameters, **path_parameters}

    body = event['body']
    headers = event['headers']
    return Request(endpoint=endpoint, method=method, parameters=parameters, body=body, headers=headers, event=event)


def event_to_web_request(event):
    event_body = event['body']
    endpoint_pattern = event_body['resource-path']
    path = event_body['params'].get('path')
    method = event_body['httpMethod']
    parameters = event_body['params'].get('querystring')
    parameters = {} if not parameters else parameters
    body = event_body['body-json']
    headers = event_body['params'].get('header')
    return WebRequest(endpoint=endpoint_pattern, path=path, method=method, parameters=parameters, body=body,
                      headers=headers, event=event_body)
