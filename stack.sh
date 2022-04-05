#!/bin/bash
# CREATE
aws cloudformation create-stack --stack-name bucketstack --template-body file://cloud_formation.yml
# UPDATE
#aws cloudformation update-stack --stack-name bucketstack --template-body file://cloud_formation.yml

aws s3 cp ./upload_S3/Reihe-22B13.csv s3://bucket-one-raw-data-2022-04-27    