from connections.redshift import RedShiftData
from connection_settings.redshift_inputs import RedShiftInputs
from connections.s3 import S3Data


inputs = RedShiftInputs('redshift-cluster-1', 'dev', 'awsuser', 20)

# print(inputs.Database)
# print(RedShiftData().execute_query())

print(S3Data().objects_list())