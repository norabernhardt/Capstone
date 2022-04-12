#!/bin/bash
# CREATE
aws cloudformation create-stack --stack-name bucketstack --template-body file://setup_buckets_dynamo.yaml
# UPDATE
#aws cloudformation update-stack --stack-name bucketstack --template-body file://setup_buckets_dynamo.yaml

sleep 5s
aws s3 cp ./upload_S3/Reihe-22B13.csv s3://bucket-two-converted-data-2022-04-27