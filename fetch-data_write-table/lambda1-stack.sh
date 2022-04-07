#!/bin/bash
# CREATE
aws cloudformation create-stack --stack-name mylambdastack --template-body file://lambda_fetch-data_write-table.yaml
# UPDATE
#aws cloudformation update-stack --stack-name mylambdastack --template-body file://lambda_fetch-data_write-table.yaml

sleep 5s
aws s3 cp ./src/code_for_zipping.zip s3://lambda-code-bucket-2022-04-27