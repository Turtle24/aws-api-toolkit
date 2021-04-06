import boto3
import json

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY

class S3Data:

    def __init__(self):
        self.client = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_KEY,
        )

    def buckets_list(self):
        response = self.client.list_buckets()
        return json.dumps(response, indent=2, default=str)

    def objects_list(self):
        response = self.client.list_objects_v2(
            Bucket='exploration-bucket',
            EncodingType='url',
            MaxKeys=100,
            FetchOwner=True,
        )
        return json.dumps(response['Contents'], indent=2, default=str)
