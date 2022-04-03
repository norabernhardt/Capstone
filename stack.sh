#!/bin/bash
# CREATE
aws cloudformation create-stack --stack-name bucketstack --template-body file://cloud_formation.yml
# UPDATE
#aws cloudformation update-stack --stack-name bucketstack --template-body file://cloud_formation.yml