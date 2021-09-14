""" Sample Python 3.8 Lambda Hello World """
import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Harness Demo",
            }
        ),
    }
