from connections.rds import RDSClient

rds = RDSClient().account_attributes()
RDSClient.pp_print(rds)


# print(s3.object_post(r'C:\Users\Aidan\aws-api-toolkit\test_s3.csv', 'test', 'exploration-bucket'))
