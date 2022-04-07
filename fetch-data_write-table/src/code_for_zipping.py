import boto3

s3client=boto3.resource("s3")
dynamodb=boto3.resource("dynamodb")
tablename="table-for-preferences"
bucketname="bucket-two-converted-data-2022-04-27"

def lambda_handler(event, context):
    bucket=s3client.Bucket(bucketname)
    for obj in bucket.objects.all():
        key=obj.key
        body=obj.get()["Body"].read()
        write_to_dynamo(body.decode("utf-8"))

def write_to_dynamo(csv_content):
    table=dynamodb.Table(tablename)
    lines=csv_content.splitlines()
    for line in lines[1:]:
        content=line.split("\t")
        table.put_item(Item={
            'title': content[0],
            'author': content[2],
            'publisher': content[3],
            'place': content[4],
            'year': content[5],
            'isbn': content[7],
            'edition': content[8],
            'pages': content[10],
            'ddc': content[19],
            'keywords': content[20],
            'table_url': content[22],
            'summary_url': content[23]
            }
        )   