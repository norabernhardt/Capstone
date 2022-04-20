import boto3
from boto3.dynamodb.conditions import Attr

dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("table-for-preferences")

def readTable():
    response=table.scan(
        FilterExpression=Attr("title").contains("Kultur") | Attr("title").contains("kultur".lower()) | \
            Attr("keywords").contains("Kultur") | Attr("keywords").contains("kultur".lower()) | \
            Attr("title").contains("Ethno") | Attr("title").contains("ethno".lower()) | \
            Attr("keywords").contains("Ethno") | Attr("keywords").contains("ethno".lower()) | \
            Attr("title").contains("Anthro") | Attr("title").contains("anthro".lower()) | \
            Attr("keywords").contains("Anthro") | Attr("keywords").contains("anthro".lower()) | \
            Attr("title").contains("Volk") | Attr("title").contains("volk".lower()) | \
            Attr("keywords").contains("Volk") | Attr("keywords").contains("volk".lower()) | \
            Attr("title").contains("Völk") | Attr("title").contains("völk".lower()) | \
            Attr("keywords").contains("Völk") | Attr("keywords").contains("völk".lower()) | \
            Attr("title").contains("Museum") | Attr("title").contains("museum".lower()) | \
            Attr("keywords").contains("Museum") | Attr("keywords").contains("museum".lower())
    )
    response["Items"]
    return response["Items"]
