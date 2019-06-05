import boto3
from handlers import decimalencoder
import json
import os

dynamodb = boto3.resource('dynamodb')

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    try:
        result = table.get_item(
            Key={
                'movie-id': event['pathParameters']['id']
            }
        )
        response = None
        if 'Item' in result.keys():
            response = {
                "statusCode": 200,
                "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder)
            } 
        else:
            response = {
                "statusCode": 404,
                "body": "Movie does not exist."
            } 
        return response
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": str(e)
        }
        return response