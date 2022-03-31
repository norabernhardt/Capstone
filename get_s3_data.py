from urllib import response
import boto3
import csv

bucketname="release-service-data-catcher101"

s3client=boto3.resource("s3")
s3_object=s3client.Bucket(bucketname).Object("Reihe-22N12.csv").get()
text=s3_object["Body"].read()
print(text)
