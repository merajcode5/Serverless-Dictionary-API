import json
import requests
import boto3
import os
from datetime import datetime

# Get table name from environment variable
HISTORY_TABLE = os.environ.get("HISTORY_TABLE")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(HISTORY_TABLE)


def lambda_handler(event, context):
    try:
        # Read word from API Gateway query parameter
        params = event.get("queryStringParameters") or {}
        word = params.get("word", "").strip()

        if not word:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Missing ?word= parameter"})
            }

        # Call dictionary API
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

        if response.status_code == 404:
            result = {"word": word, "found": False}
        else:
            result = {
                "word": word,
                "found": True,
                "results": response.json()
            }

        # Save to DynamoDB (search history)
        try:
            table.put_item(
                Item={
                    "userId": "anonymous",  
                    "timestamp": datetime.utcnow().isoformat(),
                    "word": word,
                    "result": result
                }
            )
        except Exception as db_err:
            print("DynamoDB Save Error:", db_err)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(result)
        }

    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Server error"})
        }
