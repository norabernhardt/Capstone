from urllib import response
import boto3
import csv

bucketname="release-service-data-catcher101"
# def show_s3_data(bucketname):
#     s3client=boto3.client("s3")
#     response=s3client.list_objects(
#         Bucket=bucketname
#     )
#     return(object)
# print (object)

s3client=boto3.resource("s3")
s3_object=s3client.Bucket(bucketname).Object("Reihe-22N12.csv").get()
text=s3_object["Body"].read()
print(text)

# def show_s3_data(bucketname):
#     s3client=boto3.client("s3")
#     response_list=s3client.list_objects(
#         Bucket=bucketname
#     )
#     for item in response_list["Contents"]:
#         key=item["Key"]
#         response_get=s3client.get_object(
#             Bucket=bucketname,
#             Key=key
#         )
#         text=response_get["Body"].read()
#     return text
    
#get_s3_data.show_s3_data("release-service-data-catcher101")