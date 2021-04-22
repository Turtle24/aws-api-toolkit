from connections.s3 import S3Data, S3Resource
import pathlib

s3 = S3Data()

filepath = pathlib.Path.home() / 'Downloads' / 'orders.csv'
object_name = 'Customer_Orders_2020'

resource = S3Resource()

print(resource)
