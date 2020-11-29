import punq

from src.handlers.web_handler import WebHandler


def handle_test(event, context):
    response = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'multiValueHeaders': {},
        'body': f'{str(event)}',
        'context': f'{str(context)}'
    }
    return response


container = None


def set_dependency(container):
    container.register(WebHandler, WebHandler)
    return container


def handle(event, context):
    global container
    if not container:
        container = punq.Container()
        container = set_dependency(container)
    handler = container.resolve(WebHandler)
    print(f"Processing event {event} in {context}")
    return handler.handle(event, context)
