# Movies Serverless Restful API
This example demostrates how to write a RESTful API in Python using the Serverless Framework to deploy into AWS cloud environment. The API provides a create, retrieve, update, and delete service that is used to operate on the movie data stored in DynamoDB.

## Prerequisites
* [Python 3](https://www.python.org/)
* [AWS CLI](https://aws.amazon.com/cli/)
* [NodeJS](https://nodejs.org/en/)
* [Serverless Framework](https://serverless.com/)

## API

#### GET /v1/api/movies/{movie-id}

```
curl -X GET http://hostname:port/v1/api/movies/19995
```

#### POST /v1/api/movies

```
curl -X POST \
  http://hostname:port/v1/api/movies \
  -H 'Content-Type: application/json' \
  -d '{
	"movie-id": "19995",
	"title": "Avatar",
	"budget": 237000000,
	"release-date": "2009-12-10T00:00:00Z",
	"revenue": 2787965087,
	"runtime": 162,
	"vote-average": 7.2,
	"vote-count": 11800
}'
```

#### PUT /v1/api/movies/{movie-id}

```
curl -X PUT \
  http://hostname:port/v1/api/movies/19995 \
  -H 'Content-Type: application/json' \
  -d '{
	"title": "Avatar",
	"budget": 237000000,
	"release-date": "2009-12-10T00:00:00Z",
	"revenue": 2787965087,
	"runtime": 162,
	"vote-average": 7.2,
	"vote-count": 11800
}'
```

#### DELETE /v1/api/movies/{movie-id}

```
curl -X DELETE http://hostname:port/v1/api/movies/19995 
```

## Invoke the function locally but using DynamoDB on AWS
This command invokes the get_movie function locally and pass in the data as the event.
```
serverless invoke local --function get_movie --data '{ "pathParameters" : { "id" : "1000" } }'
```

This command invokes the create_movie function locally and pass in the data as the event.
```
serverless invoke local --function create_movie --data '{ "body" : { "movie-id" : "1000", "title" : "Avatar", "budget" : 237000000, "release-date" : "2009-12-10T00:00:00Z", "revenue" : 2787965087, "runtime" : 162, "vote-average" : 7.2, "vote-count" : 11800 } }'
```

This command invokes the update_movie function locally and pass in the data as the event.
```
serverless invoke local --function update_movie --data '{ "body" : { "movie-id" : "1000", "title" : "Avatar", "budget" : 237000000, "release-date" : "2009-12-10T00:00:00Z", "revenue" : 2787965087, "runtime" : 162, "vote-average" : 7.2, "vote-count" : 11800 } }'
```

This command invokes the delete_movie function locally and pass in the data as the event.
```
serverless invoke local --function delete_movie --data '{ "pathParameters" : { "id" : "1000" } }'
```

## Run API and DynamoDB locally
This command will install the plugins needed to run the Movies API on localhost.
```
npm install serverless-offline serverless-dynamodb-local --save-dev
```

This script will start DynamoDB, create the database table defined in serverless.yml,
and start the API Gateway to expose the Movies CRUD endpoints on the localhost.
```
./run.sh
```

## Deploy to AWS
This command is used when you have updated your Function, Event or Resource configuration in serverless.yml and you want to deploy that change (or multiple changes at the same time) to a particular stage in Amazon Web Services.
```
serverless deploy --stage <dev|int|uat|prod> --verbose
```

This command will remove the deployed service in the specified stage, defined in your current working directory, from the provider.
```
serverless remove --stage <dev|int|uat|prod>
```

## Resources
* [AWS Lambda Developer Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
* [AWS DynamoDB Developer Documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
* [Boto3 API Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html)
* [Serverless Framework AWS Documentation](https://serverless.com/framework/docs/providers/aws/)
