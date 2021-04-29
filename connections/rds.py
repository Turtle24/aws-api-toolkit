import boto3
import json

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


class RDSClient:
    """Class that represents the RDS client connection"""

    def __init__(self):
        self.client = boto3.client(
            "rds",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
        )

    def __repr__(self):
        return f"RDSClient Class with properties: {self.__class__.__mro__}"

    def account_attributes(self):
        """A method that lists the account attributes of the RDS client.

        Returns:
            json: A json string of the account attributes of the client.
        """

        response = self.client.describe_account_attributes()
        return json.dumps(response, indent=2, default=str)

    def db_instances(self):
        response = self.client.describe_db_instances(
            DBInstanceIdentifier="mysql-db-project",
            MaxRecords=100,
        )
        return json.dumps(response, indent=2, default=str)


class RDSData:
    def __init__(self):
        """Class used to connect to RDS Data API."""
        self.client = boto3.client(
            "rds-data",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
        )

    def __repr__(self):
        return f"RDSData Class with properties: {self.__class__.__mro__}"

    def sql_statement(self):
        response = self.client.execute_statement(
            continueAfterTimeout=True,
            database="mysql-db-project",
            includeResultMetadata=True,
            resourceArn="arn:aws:rds:us-east-2:937543116659:db:mysql-db-project",
            resultSetOptions={
                "decimalReturnType": "STRING",
            },
            schema="Group-Project-Dev",
            awsSecretStoreArn="secret",
            sql="""SELECT * FROM `Group-Project-Dev`.US_Counties_Covid
                    ORDER BY date ASC limit 1;""",
        )
        return json.dumps(response, indent=2, default=str)
