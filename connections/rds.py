import boto3
import json

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


class RDSClient:
    """ Class that represents the RedShift Data api client connection
    """
    def __init__(self):
        self.client = boto3.client(
                'rds',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_KEY,
        )

    def account_attributes(self):
        """ A method that list the tables in the redshift database.

        Returns:
            list: A list of all the table names is return.
        """

        response = self.client.describe_account_attributes()
        return json.dumps(response, indent=2, default=str)

    def describe_tables(self, table):
        """ A method that describes the given table passed to it.

        Returns:
            json: A json string is returned that describes the table.
        """

        response = self.client.describe_table(
            ClusterIdentifier='redshift-cluster-1',
            Database='dev',
            DbUser='awsuser',
            MaxResults=20,
            Table=table
        )
        return [dicts['name'] for dicts in response['ColumnList']]

    # identify granualirity of queries
    def execute_query(self):
        """ A method that executes a query in the redshift query editor. 
        Can be used to create tables all query data.

        Returns:
            json: A json string is returned containing the success or failure 
            of the query. The actual results of the query are not returned
        """
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


class RDSData:
    def __init__(self):
        self.client = boto3.client(
                'rds-data',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_KEY,
        )

    def sql_statement(self):
        response = self.client.execute_statement(
            continueAfterTimeout=True,
            database='mysql-db-project',
            includeResultMetadata=True,
            resourceArn='arn:aws:rds:us-east-2:937543116659:db:mysql-db-project',
            resultSetOptions={
                'decimalReturnType': 'STRING',
            },
            schema='Group-Project-Dev',
            awsSecretStoreArn='secret',
            sql="SELECT * FROM `Group-Project-Dev`.US_Counties_Covid ORDER BY date ASC limit 1;",
        )
        return json.dumps(response, indent=2, default=str)
