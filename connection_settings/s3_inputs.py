from dataclasses import dataclass
from typing import Optional


@dataclass
class S3Resource:
    aws_access_key_id: str
    aws_secret_access_key: str
    bucket_name: Optional[str]
    object_name: Optional[str]


@dataclass
class S3Client(S3Resource):
    aws_access_key_id: str
    aws_secret_access_key: str
    file: Optional[str]
    bucket_name: Optional[str]


@dataclass
class S3Control(S3Resource):
    aws_access_key_id: str
    aws_secret_access_key: str
