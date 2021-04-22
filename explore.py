from connections.s3 import S3Data
import pathlib
import json

s3 = S3Data()

filepath = pathlib.Path.home() / 'Downloads' / 'orders.csv'
object_name = 'Customer_Orders_2020'
buckets = s3.buckets_list()
print(buckets)

def s3_object_upload_demo(s3, filepath, object_name, s3_bucket):
    # Client selects bucket
    selected_bucket = buckets[0]
    # Client then uploads object to desired s3 bucket
    try:
        s3.object_post(filepath, object_name, selected_bucket)
    except Exception as e:
        return f"Failed due to {e}"
    return f"Successful upload of {object_name} to {selected_bucket}"


def object_delete_demo():
    s3.object_delete(buckets[0], object_name)


print(object_delete_demo())
