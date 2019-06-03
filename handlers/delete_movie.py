import boto3
import os

dynamodb = boto3.resource('dynamodb')

def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    table.delete_item(
        Key={
            'movie-id': event['pathParameters']['id']
        }
    )
    response = {
        "statusCode": 200
    }
    return response