import datetime

create_algorithm_params = {
    "AlgorithmName": "string",
    "AlgorithmDescription": "string",
    "TrainingSpecification": {
        "TrainingImage": "string",
        "TrainingImageDigest": "string",
        "SupportedHyperParameters": [
            {
                "Name": "string",
                "Description": "string",
                "Type": ["Integer", "Continuous", "Categorical", "FreeText"],
                "Range": {
                    "IntegerParameterRangeSpecification": {
                        "MinValue": "string",
                        "MaxValue": "string",
                    },
                    "ContinuousParameterRangeSpecification": {
                        "MinValue": "string",
                        "MaxValue": "string",
                    },
                    "CategoricalParameterRangeSpecification": {
                        "Values": [
                            "string",
                        ]
                    },
                },
                "IsTunable": [True, False],
                "IsRequired": [True, False],
                "DefaultValue": "string",
            },
        ],
        "SupportedTrainingInstanceTypes": [
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.p4d.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5n.xlarge",
            "ml.c5n.2xlarge",
            "ml.c5n.4xlarge",
            "ml.c5n.9xlarge",
            "ml.c5n.18xlarge",
        ],
        "SupportsDistributedTraining": [True, False],
        "MetricDefinitions": [
            {"Name": "string", "Regex": "string"},
        ],
        "TrainingChannels": [
            {
                "Name": "string",
                "Description": "string",
                "IsRequired": [True, False],
                "SupportedContentTypes": [
                    "string",
                ],
                "SupportedCompressionTypes": [
                    "None",
                    "Gzip",
                ],
                "SupportedInputModes": [
                    "Pipe",
                    "File",
                ],
            },
        ],
        "SupportedTuningJobObjectiveMetrics": [
            {"Type": ["Maximize", "Minimize"], "MetricName": "string"},
        ],
    },
    "InferenceSpecification": {
        "Containers": [
            {
                "ContainerHostname": "string",
                "Image": "string",
                "ImageDigest": "string",
                "ModelDataUrl": "string",
                "ProductId": "string",
            },
        ],
        "SupportedTransformInstanceTypes": [
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "SupportedRealtimeInferenceInstanceTypes": [
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.24xlarge",
            "ml.c4.large",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.large",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.12xlarge",
            "ml.r5.24xlarge",
            "ml.r5d.large",
            "ml.r5d.xlarge",
            "ml.r5d.2xlarge",
            "ml.r5d.4xlarge",
            "ml.r5d.12xlarge",
            "ml.r5d.24xlarge",
            "ml.inf1.xlarge",
            "ml.inf1.2xlarge",
            "ml.inf1.6xlarge",
            "ml.inf1.24xlarge",
        ],
        "SupportedContentTypes": [
            "string",
        ],
        "SupportedResponseMIMETypes": [
            "string",
        ],
    },
    "ValidationSpecification": {
        "ValidationRole": "string",
        "ValidationProfiles": [
            {
                "ProfileName": "string",
                "TrainingJobDefinition": {
                    "TrainingInputMode": ["Pipe", "File"],
                    "HyperParameters": {"string": "string"},
                    "InputDataConfig": [
                        {
                            "ChannelName": "string",
                            "DataSource": {
                                "S3DataSource": {
                                    "S3DataType": [
                                        "ManifestFile",
                                        "S3Prefix",
                                        "AugmentedManifestFile",
                                    ],
                                    "S3Uri": "string",
                                    "S3DataDistributionType": [
                                        "FullyReplicated",
                                        "ShardedByS3Key",
                                    ],
                                    "AttributeNames": [
                                        "string",
                                    ],
                                },
                                "FileSystemDataSource": {
                                    "FileSystemId": "string",
                                    "FileSystemAccessMode": ["rw", "ro"],
                                    "FileSystemType": ["EFS", "FSxLustre"],
                                    "DirectoryPath": "string",
                                },
                            },
                            "ContentType": "string",
                            "CompressionType": ["None", "Gzip"],
                            "RecordWrapperType": ["None", "RecordIO"],
                            "InputMode": ["Pipe", "File"],
                            "ShuffleConfig": {"Seed": 123},
                        },
                    ],
                    "OutputDataConfig": {
                        "KmsKeyId": "string",
                        "S3OutputPath": "string",
                    },
                    "ResourceConfig": {
                        "InstanceType": [
                            "ml.m4.xlarge",
                            "ml.m4.2xlarge",
                            "ml.m4.4xlarge",
                            "ml.m4.10xlarge",
                            "ml.m4.16xlarge",
                            "ml.g4dn.xlarge",
                            "ml.g4dn.2xlarge",
                            "ml.g4dn.4xlarge",
                            "ml.g4dn.8xlarge",
                            "ml.g4dn.12xlarge",
                            "ml.g4dn.16xlarge",
                            "ml.m5.large",
                            "ml.m5.xlarge",
                            "ml.m5.2xlarge",
                            "ml.m5.4xlarge",
                            "ml.m5.12xlarge",
                            "ml.m5.24xlarge",
                            "ml.c4.xlarge",
                            "ml.c4.2xlarge",
                            "ml.c4.4xlarge",
                            "ml.c4.8xlarge",
                            "ml.p2.xlarge",
                            "ml.p2.8xlarge",
                            "ml.p2.16xlarge",
                            "ml.p3.2xlarge",
                            "ml.p3.8xlarge",
                            "ml.p3.16xlarge",
                            "ml.p3dn.24xlarge",
                            "ml.p4d.24xlarge",
                            "ml.c5.xlarge",
                            "ml.c5.2xlarge",
                            "ml.c5.4xlarge",
                            "ml.c5.9xlarge",
                            "ml.c5.18xlarge",
                            "ml.c5n.xlarge",
                            "ml.c5n.2xlarge",
                            "ml.c5n.4xlarge",
                            "ml.c5n.9xlarge",
                            "ml.c5n.18xlarge",
                        ],
                        "InstanceCount": 123,
                        "VolumeSizeInGB": 123,
                        "VolumeKmsKeyId": "string",
                    },
                    "StoppingCondition": {
                        "MaxRuntimeInSeconds": 123,
                        "MaxWaitTimeInSeconds": 123,
                    },
                },
                "TransformJobDefinition": {
                    "MaxConcurrentTransforms": 123,
                    "MaxPayloadInMB": 123,
                    "BatchStrategy": ["MultiRecord", "SingleRecord"],
                    "Environment": {"string": "string"},
                    "TransformInput": {
                        "DataSource": {
                            "S3DataSource": {
                                "S3DataType": [
                                    "ManifestFile",
                                    "S3Prefix",
                                    "AugmentedManifestFile",
                                ],
                                "S3Uri": "string",
                            }
                        },
                        "ContentType": "string",
                        "CompressionType": ["None", "Gzip"],
                        "SplitType": ["None", "Line", "RecordIO", "TFRecord"],
                    },
                    "TransformOutput": {
                        "S3OutputPath": "string",
                        "Accept": "string",
                        "AssembleWith": ["None", "Line"],
                        "KmsKeyId": "string",
                    },
                    "TransformResources": {
                        "InstanceType": [
                            "ml.m4.xlarge",
                            "ml.m4.2xlarge",
                            "ml.m4.4xlarge",
                            "ml.m4.10xlarge",
                            "ml.m4.16xlarge",
                            "ml.c4.xlarge",
                            "ml.c4.2xlarge",
                            "ml.c4.4xlarge",
                            "ml.c4.8xlarge",
                            "ml.p2.xlarge",
                            "ml.p2.8xlarge",
                            "ml.p2.16xlarge",
                            "ml.p3.2xlarge",
                            "ml.p3.8xlarge",
                            "ml.p3.16xlarge",
                            "ml.c5.xlarge",
                            "ml.c5.2xlarge",
                            "ml.c5.4xlarge",
                            "ml.c5.9xlarge",
                            "ml.c5.18xlarge",
                            "ml.m5.large",
                            "ml.m5.xlarge",
                            "ml.m5.2xlarge",
                            "ml.m5.4xlarge",
                            "ml.m5.12xlarge",
                            "ml.m5.24xlarge",
                        ],
                        "InstanceCount": 123,
                        "VolumeKmsKeyId": "string",
                    },
                },
            },
        ],
    },
    "CertifyForMarketplace": [True, False],
    "Tags": {"Key": "string", "Value": "string"},
}


create_model_params = {
    'ModelName': 'string',
    'PrimaryContainer': {
        'ContainerHostname': 'string',
        'Image': 'string',
        'ImageConfig': {
            'RepositoryAccessMode': ['Platform', 'Vpc'],
            'RepositoryAuthConfig': {
                'RepositoryCredentialsProviderArn': 'string'
            }
        },
        'Mode': ['SingleModel', 'MultiModel'],
        'ModelDataUrl': 'string',
        'Environment': {
            'string': 'string'
        },
        'ModelPackageName': 'string',
        'MultiModelConfig': {
            'ModelCacheSetting': ['Enabled', 'Disabled']
        }
    },
    'Containers': [
        {
            'ContainerHostname': 'string',
            'Image': 'string',
            'ImageConfig': {
                'RepositoryAccessMode': ['Platform', 'Vpc'],
                'RepositoryAuthConfig': {
                    'RepositoryCredentialsProviderArn': 'string'
                }
            },
            'Mode': ['SingleModel', 'MultiModel'],
            'ModelDataUrl': 'string',
            'Environment': {
                'string': 'string'
            },
            'ModelPackageName': 'string',
            'MultiModelConfig': {
                'ModelCacheSetting': ['Enabled', 'Disabled']
            }
        },
    ],
    'InferenceExecutionConfig': {
        'Mode': ['Serial', 'Direct']
    },
    'ExecutionRoleArn': 'string',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'VpcConfig': {
        'SecurityGroupIds': [
            'string',
        ],
        'Subnets': [
            'string',
        ]
    },
    'EnableNetworkIsolation': [True, False]
}
