import boto3
import json

class ConnectionHandler:
    
    @staticmethod
    async def rds_connection():
        rds_client = boto3.client(
        'rds',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_KEY,
        )


    @staticmethod
    async def s3_connection():
        s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_KEY,
        )

    @staticmethod
    async def redshift_connection():
        s3_client = boto3.client(
        'redshift',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_KEY,
        )

