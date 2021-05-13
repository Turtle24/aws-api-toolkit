import os
from connections.s3_master import S3ObjectOperations, S3BucketOperations

bucket = S3BucketOperations('vectest-bucket')

s3 = S3ObjectOperations(bucket.bucket)

print(s3.object_post(r'C:\Users\Aidan\aws-api-toolkit\test_s3.csv', 'test', 'exploration-bucket'))

# print(os.getcwd())