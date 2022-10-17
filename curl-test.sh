#!/bin/bash

var_post=$(curl --request POST http://localhost:5000/api/timeline_post -d 
'name=test&email=test&content=test'
{"content":"testt","created_at":"testt","email":"testt","id":1,"name":"testt"})

var_get=$(curl --request GET http://localhost:5000/api/timeline_post)

echo "post: $var_post"
echo "get: $var_get"
