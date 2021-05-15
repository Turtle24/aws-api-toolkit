import boto3
import datetime
import json

from parameters.s3_params import create_bucket_params as bucket_params
from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


class S3EndPoints:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
        )
        self.s3_control_client = boto3.client(
            "s3control",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
        )
        self.resource = boto3.resource("s3")

    def __repr__(self):
        return f"Class: {self.__class__.__name__}"


class S3BucketOperations(S3EndPoints):

    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return super().__str__() + f", Bucket name: {self.bucket.name}"

    def bucket_create(self, bucket_name) -> dict:
        bucket = self.resource.Bucket(bucket_name)
        response = bucket.create(
            ACL=bucket_params["ACL"][0],
            CreateBucketConfiguration=bucket_params["CreateBucketConfiguration"],
        )
        return json.dumps(response, indent=4)

    def buckets_list(self) -> list:
        """A method that returns the list of buckets in S3.

        Returns:
            list: A list of all the bucket names are returned.
        """
        response = self.s3_client.list_buckets()
        return [dicts["Name"] for dicts in response["Buckets"]]

    def delete_bucket(self, bucket_name) -> str:
        bucket = self.resource.Bucket(bucket_name)
        bucket.delete()
        return f"{bucket} deleted!"


class S3ObjectOperations(S3BucketOperations):

    def __init__(self):
        super().__init__()

    def object_post(self, object_path, object_name, s3_bucket):
        with open(object_path, "rb") as data:
            print("uploading")
            self.s3_client.upload_fileobj(data, s3_bucket, object_name)
            print("completed!")

    def object_put(self, file):
        response = self.s3_client.put_object(
            ACL="bucket-owner-full-control",
            Body=file,
            Bucket="exploration-bucket",
            ContentDisposition="filename-parm",
            ContentEncoding="csv",
            ContentLanguage="en",
            ContentLength=len(file),
            Expires=datetime(2022, 1, 1),
            GrantFullControl="string",
            Key="string",
        )
        return response

    # multiple delete
    def objects_delete(self):
        response = self.s3_client.bucket.delete_objects(
            Delete={
                "Objects": [
                    {"Key": "string", "VersionId": "string"},
                ],
                "Quiet": False,
            },
            MFA="string",
            RequestPayer="requester",
            ExpectedBucketOwner="string",
        )
        return response

    def objects_list(self):
        """A method that lists the objects in the S3 bucket. Parameters can be used for added granularity.
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects_v2


        Returns:
            json: A json string is returned representing the objects in the S3 bucket.
        """
        response = self.s3_client.list_objects_v2(
            Bucket="exploration-bucket",
            EncodingType="url",
            MaxKeys=100,
            FetchOwner=True,
        )
        return json.dumps(response["Contents"][0], indent=4, default=str)
