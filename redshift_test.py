import boto3
import json


from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY



client = boto3.client(
        'redshift-data',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_KEY,
        )

# response_test = redshift_client.describe_clusters(
#     ClusterIdentifier='redshift-cluster-1',
#     MaxRecords=20,
    
# )

# response = redshift_client.list_tables(
#     ClusterIdentifier='redshift-cluster-1',
#     Database='dev',
#     DbUser='awsuser',
#     MaxResults=20,
    
# )

response = client.describe_table(
            ClusterIdentifier='redshift-cluster-1',
            Database='dev',
            DbUser='awsuser',
            MaxResults=20,
        )


print(json.dumps(response, indent=2, default=str))

# results = [dicts['name'] for dicts in response['Tables']]

# print(results)