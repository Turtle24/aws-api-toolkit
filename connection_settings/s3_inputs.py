from dataclasses import dataclass
from typing import Optional

@dataclass
class S3Inputs:
    Bucket = str
    MaxKeys = int
    