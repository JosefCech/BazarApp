
def handle(event, context):
    response = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'multiValueHeaders': {},
        'body': f'{str(event)}'
    }
    return response