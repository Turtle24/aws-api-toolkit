import boto3
import datetime
from parameters.sagemaker_params import create_algorithm_params

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


class SageMakerClient:
    def __init__(self):
        self.client = boto3.client(
            "sagemaker",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
        )

    def __repr__(self):
        return f"SageMakerClient Class with properties: {self.__class__.__mro__}"

    def create_algorithm(self):
        response = self.client.create_algorithm(create_algorithm_params)
        return response

    def create_model(self, params):
        response = self.client.create_model(
            params)
        return response

    def describe_model(self):
        response = self.client.describe_model(
            ModelName='string'
        )
        return response

    def list_models(self):
        response = self.client.list_models(
            SortBy='Name'|'CreationTime',
            SortOrder='Ascending'|'Descending',
            NextToken='string',
            MaxResults=123,
            NameContains='string',
            CreationTimeBefore=datetime(2015, 1, 1),
            CreationTimeAfter=datetime(2015, 1, 1)
        )
        return response
