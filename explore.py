from parameters.s3_params import CreateBucket
from connections.s3 import S3Client, S3BatchOperations

s3 = S3BatchOperations()

print(s3)
