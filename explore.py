# from connections.redshift import RedShiftData
# from connection_settings.redshift_inputs import RedShiftInputs
from connections.rds import RDSClient, RDSData
# from connections.s3 import S3Data

# from connection_manager.aws_connection_handler import ConnectionHandler
# import json

# inputs = RedShiftInputs('redshift-cluster-1', 'dev', 'awsuser', 20)

# tables = RedShiftData().list_tables()

# table_description = RedShiftData().describe_tables(tables[0])

# # table_columns = [dicts['name'] for dicts in table_description['ColumnList']]
# print(table_description)

# print(RDSClient().account_attributes())

print(RDSData().sql_statement())

if __name__ == '__main__':
    print('main')
