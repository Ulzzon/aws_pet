import json
import os
import boto3


database = boto3.resource('dynamodb')
table = database.Table(os.environ['HITS_TABLE_NAME'])
_lambda = boto3.client('lambda')

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    table.update_item(
        Key={'path': event['path']},
        UpdateExpression='Add hits :incr',
        ExpressionAttributeValues={':incr': 1},
    )

    response = _lambda.invoke(
        FunctionName=os.environ['DOWNSTREAM_FUNCTION_NAME'],
        Payload=json.dumps(event),
    )

    body=response['Payload'].read()

    print('downstream response: '.format(body))
    return json.loads(body)