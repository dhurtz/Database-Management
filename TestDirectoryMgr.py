import unittest, os
from DirectoryMgr import DirectoryMgr

class TestDirectoryMgr (unittest.TestCase):
    def test_validateDir(self):
        directoryName = 'testFolder'
        self.assertEqual(True, DirectoryMgr.validateDir(directoryName))

    def test_makeDir(self):
        directoryName = 'makeDirFolder'
        self.assertEqual(True, DirectoryMgr.makeDir(directoryName))
        path = os.getcwd()
        path = path + '/' + directoryName
        os.rmdir(path)

    def test_removeDir(self):
        directoryName = 'makeDirFolder'
        path = os.getcwd()
        path = path + '/' + directoryName
        os.mkdir(path)
        self.assertEqual(True, DirectoryMgr.removeDir(directoryName))

    def test_validateFile(self):
        directoryName = 'testFolder'
        tableName = 'testCSV'
        self.assertEqual(True, DirectoryMgr.validateFile(tableName, directoryName))

    def test_removeFile(self):
        fileName = 'deleteCSV'
        database = 'testFolder'        
        path = os.getcwd()
        path = path + '\\' + database + '\\' + fileName + '.csv'
        file = open(path, 'a')
        file.close()
        self.assertEqual(True, DirectoryMgr.removeFile(fileName, database))
