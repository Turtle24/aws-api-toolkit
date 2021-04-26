import boto3

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


class ConnectionHandler:

    @staticmethod
    def rds_connection():
        return boto3.client(
                'rds',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_KEY,
                )

    @staticmethod
    def s3_connection():
        return boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_KEY,
                )

    @staticmethod
    def redshift_connection():
        return boto3.client(
                'redshift-data',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_KEY,
                )
