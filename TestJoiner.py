import unittest
from Joiner import Joiner

class TestJoiner(unittest.TestCase):
    def test_outerJoin(self):
        tagOne = 'Worker'
        tagTwo = 'Animal'
        firstTable = 'testCSV'
        secondTable = 'testCSV2'
        database = 'testFolder'
        resultList = [['Variable', ' Worker', ' Number', 'Integer', ' Animal', ' date'], ['int', ' User', ' 3'], ['Char', ' Clerk', ' 4'], ['string', ' Conductor', ' 6']]

        self.assertEqual(resultList, Joiner.outerJoin(tagOne, tagTwo, firstTable, secondTable, database))
    def test_innerJoin(self):
        tagOne = 'Worker'
        tagTwo = 'Animal'
        firstTable = 'testCSV'
        secondTable = 'testCSV2'
        database = 'testFolder'
        resultList = [['Variable', ' Worker', ' Number', 'Integer', ' Animal', ' date']]
        self.assertEqual(resultList, Joiner.innerJoin(tagOne, tagTwo, firstTable, secondTable, database))