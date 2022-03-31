#!/bin/bash
aws cloudformation create-stack --stack-name bucketstack --template-body file://create_s3.yml