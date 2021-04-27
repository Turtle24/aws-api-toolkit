from parameters.s3_params import CreateBucket
from connections.s3 import S3Client

create_bucket = CreateBucket('test')
print(create_bucket)

s3 = S3Client()
resp = s3.create_bucket(Bucket=create_bucket.Bucket)

print(resp)
