import boto3
from handlers import decimalencoder
import json
import os

dynamodb = boto3.resource('dynamodb')

def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    try:
        result = table.delete_item(
            Key={
                'movie-id': event['pathParameters']['id']
            },
            ExpressionAttributeNames={ "#m": "movie-id" },
            ConditionExpression="attribute_exists(#m)"
        )
        response = {
            "statusCode": 200,
            "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
        }
        return response
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": str(e)
        }
        return response