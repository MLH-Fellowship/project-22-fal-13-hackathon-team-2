#!/bin/bash

curl --request POST http://localhost:5000/api/timeline_post -d 'name=test&email=test&content=test'

curl --request GET http://localhost:5000/api/timeline_post

curl -X DELETE http://localhost:5000/api/timeline_post


