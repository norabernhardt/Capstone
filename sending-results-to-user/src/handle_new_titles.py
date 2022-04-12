import boto3
import json

client=boto3.client("sns")
ResultsSendingTopic="arn:aws:sns:eu-central-1:248461369890:ResultsSendingTopic"

def lambda_sns(event, context):
    for record in event['Records']:
        handle_new_titles(record)
    
def handle_new_titles(record):
    if 'dynamodb' in record and 'NewImage' in record['dynamodb']:
        data = get_new_image_data(record)
        if(has_relevant_title(data)):
            send_result_to_user(data)
            
def get_new_image_data(record):
    new_image=record['dynamodb']['NewImage']
    print(get_image_value(new_image, "publisher"))
    
    return{
        'title': get_image_value(new_image, "title"),
        'author': get_image_value(new_image, "author"),
        'publisher': get_image_value(new_image, "publisher"),
        'place': get_image_value(new_image, "place"),
        'year': get_image_value(new_image, "year"),
        'isbn': get_image_value(new_image, "isbn"),
        'edition': get_image_value(new_image, "edition"),
        'pages': get_image_value(new_image, "pages"),
        'ddc': get_image_value(new_image, "ddc"),
        'keywords': get_image_value(new_image, "keywords"),
        'table_url': get_image_value(new_image, "table_url"),
        'summary_url': get_image_value(new_image, "summary_url")
    }
    
def get_image_value(new_image, key):
    if key in new_image:
        return new_image[key]["S"]
    return ""
    
    
def has_relevant_title(data):
    return 'ethno' in data['title'].lower() or 'kultur' in data['keywords'].lower()

def send_result_to_user(data):
    client.publish(
        TopicArn=ResultsSendingTopic,
        Subject="New Books!",
        Message="Here are some relevant titles: " + data["author"]+"\n Titel: "+ data['title']+ \
        "\n publisher: " + data['publisher']+ " place: " + data["place"]+ \
        "\n year: " + data['year']+ \
        "\n isbn: " + data['isbn']+ \
        "\n edition: " + data['edition']+ \
        "\n pages: " + data['pages']+ \
        "\n ddc: " + data["ddc"]+ \
        "\n keywords: " + data["keywords"]+ \
        "\n table_url: " + data["table_url"]+ \
        "\n summary_url: " + data["summary_url"])