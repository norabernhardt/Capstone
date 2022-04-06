#!/bin/bash
# CREATE
aws cloudformation create-stack --stack-name mylambdastack --template-body file://lambda_fetch-data_write-table.yaml
# UPDATE
#aws cloudformation update-stack --stack-name mylambdastack --template-body file://lambda_fetch-data_write-table.yaml

aws s3 cp ./src/write_to_dynamodb.zip s3://lambda-code-bucket-2022-04-27