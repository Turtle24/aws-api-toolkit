from connections.s3 import S3Client, S3Resource
import pathlib

s3 = S3Client()

filepath = pathlib.Path.home() / 'Downloads' / 'orders.csv'
object_name = 'Customer_Orders_2020'

resource = S3Resource()

print(resource)
