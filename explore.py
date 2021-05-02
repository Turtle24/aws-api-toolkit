from connections.s3 import S3Bucket

test_bucket = S3Bucket()
print(test_bucket.create_bucket())
