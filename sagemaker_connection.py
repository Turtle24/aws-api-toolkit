import boto3
import json


from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY

client = boto3.client(
    'sagemaker',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_KEY,
)

response = client.describe_notebook_instance(
    NotebookInstanceName='TestBook'
)
print(json.dumps(response, indent=2, default=str))