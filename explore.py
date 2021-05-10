from connections.redshift import RedShiftData

red = RedShiftData()

print(red.list_databases()())
