import os
import shutil


def moveFile(source, destination):
    # Copy the content of
    # source to destination
    shutil.move(source, destination)
    print("File successfully moved. ")
