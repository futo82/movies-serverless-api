import boto3
import os

def get_dynamodb_resource():
    if "DYNAMODB_ENDPOINT" in os.environ:
        return boto3.resource('dynamodb', endpoint_url=os.environ['DYNAMODB_ENDPOINT'])
    else:
        return boto3.resource('dynamodb')
