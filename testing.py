import unittest
from connections.redshift import RedShiftData
from connections.s3 import S3Data


class RedShiftTests(unittest.TestCase):
    
    def test_list_tables(self):
        response = RedShiftData().list_tables()
        self.assertTrue(isinstance(response, list))


class S3Tests(unittest.TestCase):

    def test_buckets_list(self):
        response = S3Data().buckets_list()
        self.assertTrue(isinstance(response, list))


if __name__ == "__main__":
    unittest.main(warnings='ignore')