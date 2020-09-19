import os
import shutil
import pandas_SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine

filename = '.\\test\\test.csv'

pandas_SQLAlchemy.csv_to_sql(filename)

df = pd.read_table(filename, sep=",", error_bad_lines=False, warn_bad_lines=False)
dataFrame = pd.DataFrame(data=df)

sqlEngine = create_engine('mysql+pymysql://root:root@127.0.0.1/keyence_test_010', pool_recycle=3600)
dbConnection = sqlEngine.connect()

tableName = df.at[3, 'Program name'].lower()

try:
    frame = dataFrame.to_sql(tableName, dbConnection, if_exists='fail')
except ValueError as vx:
    print(vx)
except Exception as ex:
    print(ex)
else:
    print('Table %s created successfully.' % tableName)
finally:
    dbConnection.close()
