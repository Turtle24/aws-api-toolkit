import boto3
import json

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY

class RedShiftData:

    def __init__(self):
        self.client = boto3.client(
                'redshift-data',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_KEY,
        )

    def list_tables(self):
        response = self.client.list_tables(
            ClusterIdentifier='redshift-cluster-1',
            Database='dev',
            DbUser='awsuser',
            MaxResults=20, 
        )
        return [dicts['name'] for dicts in response['Tables']]

    # Not working
    def describe_tables(self):
        response = self.client.describe_table(
            ClusterIdentifier='redshift-cluster-1',
            Database='dev',
            DbUser='awsuser',
            MaxResults=20,
        )
        return json.dumps(response, indent=2, default=str)

    def execute_query(self):
        response = self.client.execute_statement(
            ClusterIdentifier='redshift-cluster-1',
            Database='dev',
            DbUser='awsuser',
            Sql='select * from sales',
            WithEvent=False
        )
        return json.dumps(response, indent=2, default=str)



# print(json.dumps(response, indent=2, default=str))

# response_test = redshift_client.describe_clusters(
#     ClusterIdentifier='redshift-cluster-1',
#     MaxRecords=20,
    
# )