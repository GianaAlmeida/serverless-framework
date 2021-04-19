import os
import uuid
import boto3

DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMODB_TABLE)


def hello(event, context):
    item = {
        'id': str(uuid.uuid4()),
        'message': event
    }
    return table.put_item(Item=item)
