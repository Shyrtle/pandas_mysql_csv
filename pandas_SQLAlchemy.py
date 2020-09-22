from sqlalchemy import create_engine
import pymysql
import pandas as pd
import datetime


################################################################################
#         Defining a method to call when data will need to be inserted.        #
################################################################################
def csv_to_sql(filename):
    df = pd.read_table(filename, sep=",", error_bad_lines=False, warn_bad_lines=False, engine="python")
    data_frame = pd.DataFrame(data=df)

    for b in data_frame.columns:  # Checks all columns for 'Number ' and removes the space if it finds it.
        if b.endswith(' '):  # MySQL requires no space at the end for column names.
            print("Removing extra space...")
            data_frame.rename(columns={b: b[0:len(b)-1]}, errors="raise", inplace=True)

    data_frame['Lot No.'] = data_frame['Lot No.'].astype(str)  # Changes Lot No. to string, instead of float.
    data_frame['Lot No.'] = data_frame['Lot No.'].map(lambda x: x.rstrip('.0'))
    data_frame['Name'] = data_frame['Name'].astype(str)  # Changes name to string, instead of float.
    data_frame['Name'] = data_frame['Name'].map(lambda x: x.rstrip('.0'))
    data_frame['Measurement time'] = pd.to_datetime(data_frame['Measurement time'].str.strip(), dayfirst=True)

    # <editor-fold desc="Connecting to the MySQL server.">
    sql_engine = create_engine('mysql+pymysql://root:root@127.0.0.1/keyence_test_012', pool_recycle=3600)
    db_connection = sql_engine.connect()

    table_name = df.at[3, 'Program name'].lower()  # Pulling the table name from the 3rd row of the program name column.
    # .lower() makes it lower case due to MySQL requirements.
    # </editor-fold>

    # <editor-fold desc="Inserting the .csv data into the MySQL database.">
    try:
        data_frame.to_sql(table_name, db_connection, if_exists='fail')
        # if_exists can add a new table or cancel the code.
        # 'append' makes it add the data to the existing table.
    except ValueError as vx:
        print(vx)
        print('It exists already!')
        # Drop first three rows referencing limit data.
        data_frame.drop([0, 1, 2], axis=0, inplace=True)
        try:
            data_frame.to_sql(table_name, db_connection, if_exists='append')
        except ValueError as vx:
            print(vx)
        except Exception as ex:
            print(ex)
        else:
            print('Successfully added data to table %s.' % table_name)
            print(datetime.datetime.now())

    except Exception as ex:
        print(ex)
    else:
        print('Table %s created successfully.' % table_name)
        print(datetime.datetime.now())
    finally:
        db_connection.close()  # Closing the connection to MySQL.

    # </editor-fold>
