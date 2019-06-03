import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    result = table.get_item(
        Key={
            'movie-id': event['pathParameters']['id']
        }
    )
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'])
    }
    return response