import json
import base64

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dump('Hello from Lambda modify by Git Action')
    }