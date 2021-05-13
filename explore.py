from connections.s3_master import S3BucketOperations


s3 = S3BucketOperations('vectest-bucket')

print(s3.buckets_list())
