# Manages the creation and validation of folders or files within the directory
import os

class DirectoryMgr:
    def __init__(self) -> None:
        pass

    # validates if a directory exists
    def validateDir(dirName):
        path = os.getcwd()
        path = path + '/' + dirName
        return os.path.isdir(path)
    
    # creates a directory
    def makeDir(dirName):
        path = os.getcwd()
        path = path + '/' + dirName
        return os.mkdir(path)
    
    # removes a directory
    def removeDir(dirName):
        path = os.getcwd()
        path = path + '/' + dirName
        return os.rmdir(path)

    # validates if a file exists
    def validateFile(fileName, database):
        path = os.getcwd()
        path = path + '/' + database + '/' + fileName + '.csv'
        return os.path.isfile(path)
    
    # removes a file
    def removeFile(fileName, database):
        path = os.getcwd()
        path = path + '/' + database + '/' + fileName + '.csv'
        return os.remove(path)
