import unittest
from CSVHelper import CSVHelper

class TestCSVHelper (unittest.TestCase):
    # def test_findColumn(self):
    #     findCoulumnData = [['int', 'user', 6], 
    #                        ['string', 'man', 3], 
    #                        ['float', 'clerk', 4]]
    #     self.assertTrue(1, CSVHelper.findColumn(findCoulumnData, '6'))

    def test_Convert(self):
        convertData = ['Dog', 'Lab']
        resultDict = {'Dog': 'Lab'}
        self.assertDictEqual(resultDict, CSVHelper.Convert(convertData))

    def test_findTableName(self):
        findTableNameData = 'tableName(int age, float date)'
        resultData = 'tableName'
        self.assertEqual(CSVHelper.findTableName(findTableNameData), resultData)
