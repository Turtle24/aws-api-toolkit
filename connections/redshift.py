import boto3
import json

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


class RedShiftData:
    """Class that represents the RedShift Data api client connection"""

    def __init__(self):
        self.client = boto3.client(
            "redshift-data",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
        )

    def __repr__(self):
        return f"RedShiftData Class with properties: {self.__class__.__mro__}"

    def list_databases(self):
        response = self.client.list_databases(
            ClusterIdentifier='string',
            Database='string',
            DbUser='string',
            MaxResults=123,
            NextToken='string',
            SecretArn='string'
        )
        return response

    def list_schemas(self):
        response = self.client.list_schemas(
            ClusterIdentifier='string',
            ConnectedDatabase='string',
            Database='string',
            DbUser='string',
            MaxResults=123,
            NextToken='string',
            SchemaPattern='string',
            SecretArn='string'
        )
        return response

    def list_tables(self):
        """A method that list the tables in the redshift database.

        Returns:
            list: A list of all the table names is return.
        """

        response = self.client.list_tables(
            ClusterIdentifier="redshift-cluster-1",
            Database="dev",
            DbUser="awsuser",
            MaxResults=20,
        )
        return [dicts["name"] for dicts in response["Tables"]]

    def describe_tables(self, table):
        """A method that describes the given table passed to it.

        Returns:
            json: A json string is returned that describes the table.
        """

        response = self.client.describe_table(
            ClusterIdentifier="redshift-cluster-1",
            Database="dev",
            DbUser="awsuser",
            MaxResults=20,
            Table=table,
        )
        return [dicts["name"] for dicts in response["ColumnList"]]

    def execute_statement(self):
        """A method that executes a query in the redshift query editor.
        Can be used to create tables all query data.

        Returns:
            json: A json string is returned containing the success or failure
            of the query. The actual results of the query are not returned
        """
        response = self.client.execute_statement(
            ClusterIdentifier="redshift-cluster-1",
            Database="dev",
            DbUser="awsuser",
            Sql="select * from sales",
            WithEvent=False,
        )
        return json.dumps(response, indent=2, default=str)

    def describe_statement(self):
        response = self.client.describe_statement(
            Id='string'
        )
        return response

    def cancel_statement(self):
        response = self.client.cancel_statement(
            Id='string'
        )
        return response

    def list_statements(self):
        response = self.client.list_statements(
            MaxResults=123,
            NextToken='string',
            RoleLevel=True|False,
            StatementName='string',
            Status='SUBMITTED'|'PICKED'|'STARTED'|'FINISHED'|'ABORTED'|'FAILED'|'ALL'
        )
        return response

    def get_statement_result(self):
        response = self.client.get_statement_result(
            Id='string',
            NextToken='string'
        )
        return response
