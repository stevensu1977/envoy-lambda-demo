

import json
import base64

def lambda_handler(event, context):
    # TODO implement
    body=""
    if "body" in event:
        body=event["body"]
    if "is_base64_encoded" in event and event["is_base64_encoded"]:
        body=str(base64.decodebytes(bytes(body,"utf-8")))
    return {
        'statusCode': 200,
        'body': json.dumps("hello envoy with lambda. body is: {}".format(body))
    }



