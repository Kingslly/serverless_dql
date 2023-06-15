import json

def producer(event, context):
    # Logic to push messages to the queue
    # You can use the AWS SDK to send messages to the queue
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Messages pushed to the queue"})
    }
