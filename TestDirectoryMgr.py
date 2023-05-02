import unittest
from DirectoryMgr import DirectoryMgr

class TestDirectoryMgr (unittest.TestCase):
    def test_validateDir(self):
        directoryName = 'testFolder'
        self.assertEqual(True, DirectoryMgr.validateDir(directoryName))

    def test_validateFile(self):
        directoryName = 'testFolder'
        tableName = 'testCSV'
        self.assertEqual(True, DirectoryMgr.validateFile(tableName, directoryName))

