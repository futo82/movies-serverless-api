import json
import os

from handlers import db
from handlers import decimalencoder
from handlers import util

dynamodb = db.get_dynamodb_resource()

def update(event, context):
    movie_id = event['pathParameters']['id']
    data = json.loads(event['body'])
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    item = {
        'movie-id': movie_id,
        'title': data['title'],
        'budget': data['budget'],
        'release-date': data['release-date'],
        'revenue': data['revenue'],
        'runtime': data['runtime'],
        'vote-average': util.round_float_to_decimal(data['vote-average']),
        'vote-count': data['vote-count'],
    }
    try:
        result = table.put_item(
            Item=item,
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