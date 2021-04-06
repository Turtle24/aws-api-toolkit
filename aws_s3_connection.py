import boto3
import json


from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_KEY,
)

s3_response = s3_client.list_buckets()

print(json.dumps(rds_response, indent=2, default=str))