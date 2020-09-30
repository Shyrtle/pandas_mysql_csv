import os
from time import sleep
import pandas_SQLAlchemy
import move


def initialize(paths):
    for i in paths:
        targetPath = str(i)
        for file in os.listdir(targetPath):  # For loop through directory.
            if os.path.isdir(os.path.join(targetPath, file)):
                print("Folder: ", file)
                filenameEnd = os.listdir(f"{targetPath}{file}")
                for x in filenameEnd:
                    filename = f"{targetPath}{file}\\{x}"
                    file_path = os.path.basename(filename)
                    destination = os.path.join(os.path.dirname(os.path.dirname(targetPath)), 'Keyence Backup\\', file_path)
                    print('The file is ', filename)
                    if filename.endswith('.csv'):
                        print('The file is a CSV, importing to MySQL.')
                        sleep(1)
                        print("...")
                        pandas_SQLAlchemy.csv_to_sql(filename)
                        move.moveFile(filename, destination)
                    else:
                        print(f'The file is not a .csv.')
            else:
                print(file, ' is not a folder.')
