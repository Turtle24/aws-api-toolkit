import boto3
import json
import datetime
from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


class S3Client:
    """A class that represents the S3 api connection."""

    def __init__(self):
        self.client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
        )

    def __repr__(self):
        return f"S3Client Class with properties: {self.__class__.__mro__}"

    def create_bucket(self, params):
        response = self.client.create_bucket(params)
        return response

    def buckets_list(self):
        """A method that returns the list of buckets in S3.

        Returns:
            list: A list of all the bucket names are returned.
        """
        response = self.client.list_buckets()
        return [dicts["Name"] for dicts in response["Buckets"]]

    def objects_list(self):
        """A method that lists the objects in the S3 bucket. Parameters can be used for added granularity.
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects_v2


        Returns:
            json: A json string is returned representing the objects in the S3 bucket.
        """
        response = self.client.list_objects_v2(
            Bucket="exploration-bucket",
            EncodingType="url",
            MaxKeys=100,
            FetchOwner=True,
        )
        return response["Contents"]

    def object_post(self, object_path, object_name, s3_bucket):
        with open(object_path, "rb") as data:
            print("uploading")
            self.client.upload_fileobj(data, s3_bucket, object_name)
            print("completed!")

    def object_put(self, file):
        response = self.client.put_object(
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
        response = self.client.bucket.delete_objects(
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


class S3Control:
    """AWS S3 Control provides access to Amazon S3 control plane actions."""

    def __init__(self):
        self.client = boto3.client(
            "s3control",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
        )

    def __repr__(self):
        return f"S3Control Class with properties: {self.__class__.__mro__}"

    def bucket_get(self):
        response = self.client.get_bucket(
            AccountId="937543116659", Bucket="exploration-bucket"
        )
        return json.dumps(response, indent=2, default=str)


class S3Resource:
    """Class representing the S3 Resources. Buckets and Objects fall under this class."""

    def __init__(self):
        self.resource = boto3.resource(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
        )

    def __repr__(self):
        return f"S3Resource Class with properties: {self.__class__.__mro__}"

    def object_delete(self, bucket_name, object_name):
        del_obj = self.resource.Object(bucket_name, object_name)
        response = del_obj.delete()
        return response

    # single bucket delete
    def bucket_delete(self, bucket_name):
        try:
            self.resource.Bucket(bucket_name).delete()
        except Exception as e:
            return f"Bucket Name: {bucket_name} - Failed to delete due to {e}"
        return f"Bucket Name: {bucket_name} - successfuly deleted"


class S3BatchOperations(S3Control):
    """Class representing S3 Batch Operations. For example jobs."""

    def __repr__(self):
        return f"S3Client Child Class with properties: {self.__class__.__mro__}"

    def jobs_list(self):
        response = self.client.list_jobs(
            AccountId="string",
            JobStatuses=[
                "Active"
                | "Cancelled"
                | "Cancelling"
                | "Complete"
                | "Completing"
                | "Failed"
                | "Failing"
                | "New"
                | "Paused"
                | "Pausing"
                | "Preparing"
                | "Ready"
                | "Suspended",
            ],
            NextToken="string",
            MaxResults=123,
        )
        return response

    def job_create(self):
        response = self.client.create_job(None)
        return response

