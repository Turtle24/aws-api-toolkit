from connections.redshift import RedShiftData
from connection_settings.redshift_inputs import RedShiftInputs
from connections.s3 import S3Data

from connection_manager.aws_connection_handler import ConnectionHandler


# inputs = RedShiftInputs('redshift-cluster-1', 'dev', 'awsuser', 20)

# print(inputs.Database)
# print(RedShiftData().execute_query())

# print(S3Data().buckets_list())

# async def test():
#     con = await ConnectionHandler.redshift_connection()
#     return con.client.describe_table(
#             ClusterIdentifier='redshift-cluster-1',
#             Database='dev',
#             DbUser='awsuser',
#             MaxResults=20,
#         )

print(ConnectionHandler.redshift_connection().list_tables(
            ClusterIdentifier='redshift-cluster-1',
            Database='dev',
            DbUser='awsuser',
            MaxResults=20, 
        )
)