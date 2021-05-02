import datetime

"""Parameter variables for S3ClientBucket bucket methods.
"""

create_bucket_params = {
    'ACL': ['private', 'public-read', 'public-read-write', 'authenticated-read'],
    'CreateBucketConfiguration': {
        'LocationConstraint': ['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'EU', 'eu-central-1', 'eu-north-1', 'eu-south-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-south-1', 'sa-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-west-1', 'us-west-2']
    },
    'GrantFullControl': 'string',
    'GrantRead': 'string',
    'GrantReadACP': 'string',
    'GrantWrite': 'string',
    'GrantWriteACP': 'string',
    'ObjectLockEnabledForBucket': [True, False]
}

"""Parameter variables for S3Client batch methods.
"""

s3_batch_job_create = {
    'AccountId': "string",
    'ConfirmationRequired': True | False,
    'Operation': {
        "LambdaInvoke": {"FunctionArn": "string"},
        "S3PutObjectCopy": {
            "TargetResource": "string",
            "CannedAccessControlList": "private"
            | "public-read"
            | "public-read-write"
            | "aws-exec-read"
            | "authenticated-read"
            | "bucket-owner-read"
            | "bucket-owner-full-control",
            "AccessControlGrants": [
                {
                    "Grantee": {
                        "TypeIdentifier": "id" | "emailAddress" | "uri",
                        "Identifier": "string",
                        "DisplayName": "string",
                    },
                    "Permission": "FULL_CONTROL"
                    | "READ"
                    | "WRITE"
                    | "READ_ACP"
                    | "WRITE_ACP",
                },
            ],
            "MetadataDirective": "COPY" | "REPLACE",
            "ModifiedSinceConstraint": datetime(2015, 1, 1),
            "NewObjectMetadata": {
                "CacheControl": "string",
                "ContentDisposition": "string",
                "ContentEncoding": "string",
                "ContentLanguage": "string",
                "UserMetadata": {"string": "string"},
                "ContentLength": 123,
                "ContentMD5": "string",
                "ContentType": "string",
                "HttpExpiresDate": datetime(2015, 1, 1),
                "RequesterCharged": True | False,
                "SSEAlgorithm": "AES256" | "KMS",
            },
            "NewObjectTagging": [
                {"Key": "string", "Value": "string"},
            ],
            "RedirectLocation": "string",
            "RequesterPays": True | False,
            "StorageClass": "STANDARD"
            | "STANDARD_IA"
            | "ONEZONE_IA"
            | "GLACIER"
            | "INTELLIGENT_TIERING"
            | "DEEP_ARCHIVE",
            "UnModifiedSinceConstraint": datetime(2015, 1, 1),
            "SSEAwsKmsKeyId": "string",
            "TargetKeyPrefix": "string",
            "ObjectLockLegalHoldStatus": "OFF" | "ON",
            "ObjectLockMode": "COMPLIANCE" | "GOVERNANCE",
            "ObjectLockRetainUntilDate": datetime(2015, 1, 1),
        },
        "S3PutObjectAcl": {
            "AccessControlPolicy": {
                "AccessControlList": {
                    "Owner": {"ID": "string", "DisplayName": "string"},
                    "Grants": [
                        {
                            "Grantee": {
                                "TypeIdentifier": "id" | "emailAddress" | "uri",
                                "Identifier": "string",
                                "DisplayName": "string",
                            },
                            "Permission": "FULL_CONTROL"
                            | "READ"
                            | "WRITE"
                            | "READ_ACP"
                            | "WRITE_ACP",
                        },
                    ],
                },
                "CannedAccessControlList": "private"
                | "public-read"
                | "public-read-write"
                | "aws-exec-read"
                | "authenticated-read"
                | "bucket-owner-read"
                | "bucket-owner-full-control",
            }
        },
        "S3PutObjectTagging": {
            "TagSet": [
                {"Key": "string", "Value": "string"},
            ]
        },
        "S3DeleteObjectTagging": {},
        "S3InitiateRestoreObject": {
            "ExpirationInDays": 123,
            "GlacierJobTier": "BULK" | "STANDARD",
        },
        "S3PutObjectLegalHold": {"LegalHold": {"Status": "OFF" | "ON"}},
        "S3PutObjectRetention": {
            "BypassGovernanceRetention": True | False,
            "Retention": {
                "RetainUntilDate": datetime(2015, 1, 1),
                "Mode": "COMPLIANCE" | "GOVERNANCE",
            },
        },
    },
    'Report': {
        "Bucket": "string",
        "Format": "Report_CSV_20180820",
        "Enabled": True | False,
        "Prefix": "string",
        "ReportScope": "AllTasks" | "FailedTasksOnly",
    },
    'ClientRequestToken': "string",
    'Manifest': {
        "Spec": {
            "Format": "S3BatchOperations_CSV_20180820"
            | "S3InventoryReport_CSV_20161130",
            "Fields": [
                "Ignore" | "Bucket" | "Key" | "VersionId",
            ],
        },
        "Location": {
            "ObjectArn": "string",
            "ObjectVersionId": "string",
            "ETag": "string",
        },
    },
    'Description': "string",
    'Priority': 123,
    'RoleArn': "string",
    'Tags': [
        {"Key": "string", "Value": "string"},
    ],
}