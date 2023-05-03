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

    def test_readSpecificValuesNotEqual(self):
        valuesNotEqualFile = 'valuesNotEqual'
        database = 'testFolder'
        secondColumn = 'Weight'
        thirdColumn = 'Name'
        firstColumn = 'Age'
        value = '21'
        self.assertTrue('60 John', ModifyCSV.readSpecificValuesNotEqual(valuesNotEqualFile, database, firstColumn, secondColumn, thirdColumn, value))

    def test_changeValueWithSameColumn(self):
        sameColumnFile = 'sameColumn'
        database = 'testFolder'
        oldValue = '21'
        newValue = '25'
        output = [['String Name', 'Int Age', 'Float Weight'], ['Dustin', ' 21', ' 150'], ['John', ' 22', ' 60'], ['Ben', ' 22', ' 210']]
        self.assertEqual(output, ModifyCSV.changeValueWithSameColumn(sameColumnFile, database, oldValue, newValue))    


    def test_changeValueWithDifferentColumn(self):
        changeColumnFile = 'changeColumn'
        database = 'testFolder'
        oldValue = '150'
        newValue = '25'
        columnName = 'Age'
        output = [['String Name', 'Int Age', 'Float Weight'], ['Dustin', '25', '150'], ['John', '19', '60'], ['Ben', '24', '210']]
        self.assertEqual(output, ModifyCSV.changeValueWithDifferentColumn(changeColumnFile, database, oldValue, newValue, columnName))

    # def test_deleteValuesEqual(self):
    
    # def test_deleteValuesGreater(self):

    # def test_removeOuterParentheses(self):