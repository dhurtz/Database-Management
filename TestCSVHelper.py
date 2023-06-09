import unittest, os, csv, sys
from CSVHelper import CSVHelper
from io import StringIO

class TestCSVHelper (unittest.TestCase):
    def test_findColumn(self):
        path = os.getcwd()
        path = path  + '/testFolder/testCSV.csv'
        with open(path, 'r', newline='') as file_one:
            reader = csv.reader(file_one)
            data_1 = list(reader)
            file_one.close()
        self.assertTrue(3, CSVHelper.findColumn(data_1, '3'))

    def test_Convert(self):
        convertData = ['Dog', 'Lab']
        resultDict = {'Dog': 'Lab'}
        self.assertDictEqual(resultDict, CSVHelper.Convert(convertData))

    def test_findTableName(self):
        findTableNameData = 'tableName(int age, float date)'
        resultData = 'tableName'
        self.assertEqual(CSVHelper.findTableName(findTableNameData), resultData)

    def test_printList(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        list = ['dog', 'cat', 'bear']
        printStatement = 'dog | cat | bear |'
        self.assertTrue(printStatement, CSVHelper.printList(list))