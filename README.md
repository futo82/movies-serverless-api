# Movies Serverless Restful API
This example demostrates how to write a RESTful API in Python using the Serverless Framework to deploy into AWS cloud environment. The API provides a create, retrieve, update, and delete service that is used to operate on the movie data stored in DynamoDB.

## Prerequisites
npm install -g serverless

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

## Invoke the functions locally
This command invokes the get_movie function locally and pass in the data as the event.
```
serverless invoke local --function get_movie --data '{"id" : "12345"}'
```

This command invokes the create_movie function locally and pass in the data as the event.
```
serverless invoke local --function create_movie --data '{"id" : "12345"}'
```

This command invokes the delete_movie function locally and pass in the data as the event.
```
serverless invoke local --function delete_movie --data '{"id" : "12345"}'
```

## Run API and DynamoDB locally
This command will install the plugins needed to run the Movies API on localhost.
```
npm install serverless-offline serverless-dynamodb-local --save-dev
```

This command will start DynamoDB, create the databas table defined in server.yml,
and start the API Gateway to expose the Movies CRUD endpoints on the localhost.
```
serverless offline start -r us-east-1 --noTimeout
```
