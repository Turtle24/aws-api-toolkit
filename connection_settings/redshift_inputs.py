from dataclasses import dataclass
from typing import Optional

@dataclass
class RedShiftInputs:
    ClusterIdentifier: str
    Database: str
    DbUser: str
    MaxResults: int

@dataclass
class RedShiftSQL(RedShiftInputs):
    Sql: str
    StatementName = Optional[str]
    WithEvent=Optional[bool]