from dataclasses import dataclass
from typing import Optional


@dataclass
class RedShiftInputs:
    clusterIdentifier: str
    database: str
    dbUser: str
    maxResults: int
    table: str


@dataclass
class RedShiftSQL(RedShiftInputs):
    sql: str
    statementName: Optional[str]
    withEvent: Optional[bool]
