from connections.s3 import S3Control

print(S3Control().bucket_get())

if __name__ == '__main__':
    print('main')
