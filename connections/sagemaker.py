import boto3
import json
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
        return f"SageMakerClient Class with properties: {dir(self)[27:]}"

    def create_algorithm(self):
        response = self.client.create_algorithm(create_algorithm_params)
        return response
