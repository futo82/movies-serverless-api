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
                    Item=record['dynamodb']['NewImage'],
                    ExpressionAttributeNames={ "#m": "movie-id" },
                    ConditionExpression="attribute_not_exists(#m)"
                )
            else:
               print(record['eventID'])
               print(record['eventName'])
               print("DynamoDB Record: " + json.dumps(record['dynamodb'], indent=2))
            num_processed = num_processed + 1
        except Exception as e:
            print("Failed to process record: " + json.dumps(record['dynamodb'], indent=2))
            print(str(e))
    return 'Successfully processed {} records.'.format(num_processed)
