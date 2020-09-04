import os
import move
import remoteConnect
import testRemote

# remoteConnect.remote_connect('10.0.3.61')

# os.listdir('\\\\sei_files\\ACTIVE INSPECTION PROGRAMS\\PLATING\\Keyence\\')

# os.listdir('\\\\10.0.3.61\\')


# paths = ['\\\\10.0.3.61\\IMSeriesShared\\MSetting\\', '\\\\10.0.0.42\\sei_files\\Quality\\ACTIVE INSPECTION PROGRAMS\\PLATING\\Keyence\\']
#
#
# for i in paths:
#     targetPath = str(i)
#     checkPath = targetPath[:1]
#     print(checkPath)
#     if checkPath == '\\':
#         netPath = targetPath.split("\\")
#         networkPath = netPath[2]
#         print(f'Connecting to {networkPath}')
#         remoteConnect.remote_connect(networkPath)
#     else:
#         print(f'{targetPath} is a local path. No network connection required.')

hostName1 = "10.0.3.61"
shareName1 = "IMSeriesShared"

hostName2 = "10.0.0.42"
shareName2 = "sei_files"


# testRemote.remote_connect(hostName, shareName)
# testRemote.remote_connect(hostName2, shareName2)

hostName = ['10.0.3.61','10.0.0.42']
shareName = ['IMSeriesShared','sei_files']

path = '\\\\10.0.3.61\\IMSeriesShared\\MSetting\\'
path2 = '\\\\sei_files\\quality\\'

# testRemote.remote_connect('10.0.3.61', 'IMSeriesShared')
# testRemote.remote_connect('10.0.0.42', 'sei_files')

for i in range(len(hostName)):
    targetHost=hostName[i]
    targetShare = shareName[i]
    print(targetHost, targetShare)
    testRemote.remote_connect(targetHost, targetShare)

print(os.listdir('\\\\sei_files\\quality\\ACTIVE INSPECTION PROGRAMS\\PLATING\\Keyence\\'))
print("##############################################################")
print(os.listdir('\\\\10.0.3.61\\IMSeriesShared\\MSetting\\'))

# for i in hostName, shareName:
#     targetHost = hostName[i]
#     targetShare = shareName[i]
#     remoteConnect.remote_connect(targetHost, targetShare)
