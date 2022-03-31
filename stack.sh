#!/bin/bash
# CREATE
aws cloudformation create-stack --stack-name bucketstack --template-body file://create_s3.yml
# UPDATE
#aws cloudformation update-stack --stack-name bucketstack --template-body file://create_s3.yml