import unittest
from ModifyCSV import ModifyCSV

class TestModifyCSV(unittest.TestCase):
    def test_writeHeaders(self):
        headerFile = 'headerFile'
        database = 'testFolder'
        testDict = {'String': 'Name', 'Int': 'Age', 'Float': 'Weight'}
        self.assertEqual(1, ModifyCSV.writeHeaders(headerFile, database, testDict))

    def test_insertValues(self):
        headerFile = 'headerFile'
        database = 'testFolder'
        values = ['Dustin', '21', '150']
        self.assertEqual(1, ModifyCSV.insertValues(headerFile, database, values))
    
    def test_readFile(self):
        headerFile = 'headerFile'
        database = 'testFolder'
        self.assertEqual(1, ModifyCSV.readFile(headerFile, database))

    # def test_readSpecificValuesNotEqual(self):

    
    # def test_changeValueWithSameColumn(self):

    # def test_changeValueWithDifferentColumn(self):
    
    # def test_deleteValuesEqual(self):
    
    # def test_deleteValuesGreater(self):

    # def test_removeOuterParentheses(self):