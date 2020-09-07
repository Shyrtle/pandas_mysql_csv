import win32wnet
import pywintypes
import sys
import os


# <editor-fold desc="Used to connect to network drive">


def remote_connect(hostName, shareName):  # hostName should be the IP for the network desired

    CONNECT_INTERACTIVE = 0x00000008

    HOST_NAME = hostName  # Host IP Address
    SHARE_NAME = shareName  # Host Server Name
    SHARE_FULL_NAME = os.path.sep * 2 + os.path.sep.join((HOST_NAME, SHARE_NAME))
    SHARE_USER = "im-user"  # Host username (if required)
    SHARE_PWD = "32032"  # Host Password (if required)

    def main():
        net_resource = win32wnet.NETRESOURCE()
        net_resource.lpRemoteName = SHARE_FULL_NAME
        flags = 0
        # flags |= CONNECT_INTERACTIVE
        print("Trying to create connection to: {:s}".format(SHARE_FULL_NAME))
        try:
            win32wnet.WNetAddConnection2(net_resource, SHARE_PWD, SHARE_USER, flags)  # Connect to network
        except pywintypes.error as e:
            print(e)
        else:
            print("Success!")

    if __name__ == "__main__":
        print("Python {:s} on {:s}\n".format(sys.version, sys.platform))
        main()

# </editor-fold>
