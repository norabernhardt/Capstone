import boto3

client=boto3.client("sns")
topic_arn="arn:aws:sns:eu-central-1:248461369890:SnsRelevantTitles"

def lambda_sns(event, context):
    for record in event['Records']:
        handle_new_titles(record)
    
def handle_new_titles(record):
    if 'dynamodb' in record and 'NewImage' in record['dynamodb']:
        data = get_new_image_data(record)
        if(relevant_title(data)):
            send_result_to_user(data)
            
def get_new_image_data(record):
    new_image=record['dynamodb']['NewImage']
    
    return{
        'title': new_image,
        'author': new_image,
        'publisher': new_image,
        'place': new_image,
        'year': new_image,
        'isbn': new_image,
        'edition': new_image,
        'pages': new_image,
        'ddc': new_image,
        'keywords': new_image,
        'table_url': new_image,
        'summary_url': new_image
    }
    
def relevant_title(data):
    return 'nora' in data['title'] or 'nora' in data['author']

def send_result_to_user(data):
    print("New publications have been listet! " + data['title'])
    client.publish(
        TopicArn=topic_arn,
        Subject="New Books",
        Message="Here are some relevant titles: " + data['title']+ \
        "\n author: " + data['author']+ \
        "\n publisher: " + data['publisher,']+ " place: " + data["place"]+ \
        "\n year: " + data['year']+ \
        "\n isbn: " + data['isbn']+ \
        "\n edition: " + data['edition']+ \
        "\n pages: " + data['pages']+ \
        "\n ddc: " + data["ddc"]+ \
        "\n keywords: " + data["keywords"]+ \
        "\n table_url: " + data["table_url"]+ \
        "\n summary_url: " + data["summary_url"])