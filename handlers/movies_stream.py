import json
import os

from handlers import db

dynamodb = db.get_dynamodb_resource()

def process(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    num_processed = 0
    for record in event['Records']:
        try:
            if record['eventName'] == 'INSERT':
                table.put_item(
                    Item=build_item(record['dynamodb']['NewImage']),
                    ExpressionAttributeNames={ "#m": "movie-id" },
                    ConditionExpression="attribute_not_exists(#m)"
                )
                print("Successfully inserted movie '" + get_key(record) + "'.")
            elif record['eventName'] == 'MODIFY':
                table.put_item(
                    Item=build_item(record['dynamodb']['NewImage']),
                    ExpressionAttributeNames={ "#m": "movie-id" },
                    ConditionExpression="attribute_exists(#m)"
                )
                print("Successfully modified movie '" + get_key(record) + "'.")
            elif record['eventName'] == 'REMOVE':
                table.delete_item(
                    Key={
                        'movie-id': get_key(record)
                    },
                    ExpressionAttributeNames={ "#m": "movie-id" },
                    ConditionExpression="attribute_exists(#m)"
                )
                print("Successfully removed movie '" + get_key(record) + "'.")
            else:
                print('Event {} is not supported for record {}'.format(record['eventName'], record['dynamodb']))
            num_processed = num_processed + 1
        except Exception as e:
            print("Failed to process record: " + json.dumps(record['dynamodb'], indent=2))
            print(str(e))
    return 'Successfully processed {} records.'.format(num_processed)

def build_item(new_image):
    return {
        'movie-id': new_image['movie-id']['S'],
        'title': new_image['title']['S'],
        'budget': new_image['budget']['N'],
        'release-date': new_image['release-date']['S'],
        'revenue': new_image['revenue']['N'],
        'runtime': new_image['runtime']['N'],
        'vote-average': new_image['vote-average']['N'],
        'vote-count': new_image['vote-count']['N'],
    }

def get_key(record):
    return record['dynamodb']['Keys']['movie-id']['S']

