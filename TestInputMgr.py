import unittest
from InputMgr import InputMgr

class TestInputMgr (unittest.TestCase):
    def test_createDatabase(self):
        line_list = ['CREATE', 'DATABASE', 'testInputFolder']
        self.assertEqual(1, InputMgr.createDatabase(line_list))
        fail_list = ['']
        self.assertEqual(0, InputMgr.createDatabase(fail_list))

    def test_createTable(self):
        directory = 'testFolder'
        line = "Create Table MyTable(String Name, Int Age, Float Weight)"
        self.assertEqual(1, InputMgr.createTable(directory, line))

        fail_line = ''
        self.assertEqual(0, InputMgr.createTable(directory, fail_line))
    
    def test_deleteDatabase(self):
        line_list = ['DELETE', 'DATABASE', 'deleteFolder']
        self.assertEqual(1, InputMgr.deleteDatabase(line_list))

        fail_list = ['']
        self.assertEqual(0, InputMgr.deleteDatabase(fail_list))

    def test_removeTable(self):
        database = 'testFolder'
        line_list = ['DROP', 'TABLE', 'dropTable']
        self.assertEqual(1, InputMgr.removeTable(line_list, database))

        fail_list = ['']
        self.assertEqual(0, InputMgr.removeTable(fail_list))
    
    def test_selectTable(self):
        database = 'testFolder'
        line_list = ['SELECT', '*', 'FROM', 'headerFile']
        self.assertEqual(1, InputMgr.selectTable(line_list, database))

        fail_list = ['']
        self.assertEqual(0, InputMgr.selectTable(fail_list, database))

