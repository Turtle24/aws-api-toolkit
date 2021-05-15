import unittest
from connections.s3_master import S3BucketOperations, S3ObjectOperations
from connections.rds import RDSClient


class RDSTests(unittest.TestCase):

    def test_account_attributes(self):
        response = RDSClient().account_attributes()
        self.assertTrue(isinstance(response, dict))


class S3Tests(unittest.TestCase):

    def test_buckets_list(self):
        response = S3BucketOperations().buckets_list()
        self.assertTrue(isinstance(response, list))

    def test_create_delete(self):
        response = S3BucketOperations().bucket_create('bucket-vectice')
        self.assertTrue(response, 'bucket-vectice')

    def test_delete(self):
        response = S3BucketOperations().delete_bucket('bucket-vectice')
        self.assertTrue(response, "bucket-vectice deleted!")


class S3ObjectsTest(unittest.TestCase):

    def test_objects_list(self):
        response = S3ObjectOperations().objects_list()
        self.assertTrue(isinstance(response, list))


if __name__ == "__main__":
    unittest.main(warnings='ignore')
