from urllib import response
import boto3
import csv

bucketname="bucket-two-converted-data-2022-04-27"

s3client=boto3.resource("s3")
s3_object=s3client.Bucket(bucketname).Object("Reihe-22N12.csv").get()
text=s3_object["Body"].read()
print(text)
