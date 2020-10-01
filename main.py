import time
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import move
import pandas_SQLAlchemy
import remoteConnect
import initialize


#  When changes are made in the declared folder or any subfolders, the file
#  will be detected, and added to the MySQL database.
class MyHandler(FileSystemEventHandler):
    file_cache = {}

    def on_created(self, event):
        seconds = int(time.time())
        key = (seconds, event.src_path)
        if key in self.file_cache:
            return
        self.file_cache[key] = True
        file_path = os.path.basename(event.src_path)
        source = event.src_path
        destination = os.path.join(os.path.dirname(os.path.dirname(targetPath)), 'Keyence Backup\\', file_path)
        print(f"{event.src_path} was added to the folder.")
        if event.src_path.endswith('.csv'):
            print('The file is a CSV, importing to MySQL.')
            sleep(1)
            print('...')
            pandas_SQLAlchemy.csv_to_sql(event.src_path)
            sleep(1)
            print("...")

            move.moveFile(source, destination)  # Calling the method to move the file.
        else:
            print(f'The file is not a .csv.')


# <editor-fold desc="Select which paths to watch, if they are network drives connect to them, and start watching.">

paths = ['\\\\sei_files\\Quality\\ACTIVE INSPECTION PROGRAMS\\ASSEMBLY QC-GAGE INSP. PROGRAMS\\Keyence IM\\', '\\\\sei_files\\Quality\\ACTIVE INSPECTION PROGRAMS\\PLATING\\Keyence\\']
hostName = ['10.0.3.61','10.0.0.42']
shareName = ['IMSeriesShared','sei_files']
event_handler = MyHandler()
observer = Observer()

for i in range(len(hostName)):
    targetHost = hostName[i]
    targetShare = shareName[i]
    remoteConnect.remote_connect(targetHost, targetShare)

# for i in paths:
#     targetPath = str(i)
#     checkPath = targetPath[:1]
#     if checkPath == '\\':
#         netPath = targetPath.split("\\")
#         networkPath = netPath[2]
#         print(f'Connecting to {networkPath}')
#         remoteConnect.remote_connect(hostName, shareName)
#     else:
#         print(f'{targetPath} is a local path. No network connection required.')

initialize.initialize(paths)

for i in paths:
    targetPath = str(i)
    observer.schedule(event_handler, targetPath, recursive=True)
    #observer.start()
# By setting recursive = True, we are letting the program watch subfolders as well as the main folder.
observer.start()
print('Observer starting. Waiting for file to move...')
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
# </editor-fold>
