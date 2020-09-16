import os
import move
import pandas_SQLAlchemy
import remoteConnect

# <editor-fold desc="Goes through each folder and imports .csv files into the MySQL database">
basepaths = ['\\\\10.0.3.61\\IMSeriesShared\\MSetting\\',
             '\\\\10.0.3.72\\IMSeriesShared\\MSetting\\']

# Add remoteConnect method for each basepath. Connect to all required servers if the password and username are the same.
for i in basepaths:
    targetPath = str(i)
    checkPath = targetPath[:1]
    if checkPath == '\\':
        netPath = targetPath.split("\\")
        networkPath = netPath[2]
        print(f'Connecting to {networkPath}')
        remoteConnect.remote_connect(networkPath)
    else:
        print(f'{targetPath} is a local path. No network connection required.')


# <editor-fold desc="Loop through all files on startup and add and move any that are csv files.">

for i in basepaths:
    targetPath = str(i)
    for file in os.listdir(targetPath):  # For loop through directory.
        if os.path.isdir(os.path.join(targetPath, file)):
            print("Folder: ", file)
            filenameEnd = os.listdir(f"{targetPath}{file}")
            for x in filenameEnd:
                filename = f"{targetPath}{file}\\{x}"
                file_path = os.path.basename(filename)
                destination = f"C:\\PythonMySQL\\backup\\{file_path}"
                print('The file is ', filename)
                if filename.endswith('.csv'):
                    print('The file is a CSV, importing to MySQL.')
                    pandas_SQLAlchemy.csv_to_sql(filename)
                    move.moveFile(filename, destination)
                else:
                    print(f'The file is not a .csv.')
        else:
            print(file, ' is not a folder.')
# </editor-fold>
# </editor-fold>
