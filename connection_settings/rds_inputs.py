from dataclasses import dataclass
from typing import Optional


@dataclass
class RDSClientInputs:
    """Class for RDS Client connections.
    """
    ClusterIdentifier: str
    Database: str
    DbUser: str
    MaxResults: Optional[int]
    Table: str


@dataclass
class RDSDataInputs:
    """Class for RDS Data API connections.
    """
    database: str
    includeResultMetadata: bool
    resourceArn: str
    schema: str
    awsSecretStoreArn: str
    sql: str
