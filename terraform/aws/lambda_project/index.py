import json

def lambda_handler(event, context):
    for record in event['Records']:
        message_body = record['body']
        print(f"Received message: {message_body}")
        try:
            message = json.loads(message_body)
            print(f"Parsed message: {message}")
        except json.JSONDecodeError:
            print("Message is not in JSON format")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed successfully!')
    }