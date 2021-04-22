import boto3
import json
import datetime
from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


class S3Data:
    """ A class that represents the S3 api connection.
    """
    def __init__(self):
        self.client = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_KEY,
        )

    def buckets_list(self):
        """ A method that returns the list of buckets in S3.

        Returns:
            list: A list of all the bucket names are returned.
        """
        response = self.client.list_buckets()
        return [dicts['Name'] for dicts in response['Buckets']]

    def objects_list(self):
        """ A method that lists the objects in the S3 bucket. Parameters can be used for added granularity. 
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects_v2


        Returns:
            json: A json string is returned representing the objects in the S3 bucket.
        """
        response = self.client.list_objects_v2(
            Bucket='exploration-bucket',
            EncodingType='url',
            MaxKeys=100,
            FetchOwner=True,
        )
        return json.dumps(response['Contents'], indent=2, default=str)

    def object_post(self, object_path, object_name, s3_bucket):
        with open(object_path, 'rb') as data:
            print('uploading')
            self.client.upload_fileobj(data, s3_bucket, object_name)
            print('completed!')

    def object_put(self, file):
        response = self.client.put_object(
                ACL='bucket-owner-full-control',
                Body=file,
                Bucket='exploration-bucket',
                ContentDisposition='filename-parm',
                ContentEncoding='csv',
                ContentLanguage='en',
                ContentLength=len(file),
                Expires=datetime(2022, 1, 1),
                GrantFullControl='string',
                Key='string',
            )
        return response

    def object_delete(self):
        pass


class S3Control:
    def __init__(self):
        self.client = boto3.client(
                's3control',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_KEY,
        )

    def bucket_get(self):
        response = self.client.get_bucket(
            AccountId='937543116659',
            Bucket='exploration-bucket'
            )
        return json.dumps(response, indent=2, default=str)
