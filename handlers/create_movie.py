import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event['body'])
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    item = {
        'movie-id': data['movie-id'],
        'title': data['title'],
        'budget': data['budget'],
        'release-date': data['release-date'],
        'revenue': data['revenue'],
        'runtime': data['runtime'],
        'vote-average': data['vote-average'],
        'vote-count': data['vote-count'],
    }
    table.put_item(Item=item)
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    return response