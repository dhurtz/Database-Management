from DirectoryMgr import DirectoryMgr
from Joiner import Joiner
from CSVHelper import CSVHelper
from ModifyCSV import ModifyCSV
# Handles all the input from the user

class InputMgr:
    def __init__(self) -> None:
        pass

    def readInput(self):
        
        print('Please Enter a command \n'
            'Enter .EXIT to close program')
        line = input()
        current_directory = ''
        while (line != '.EXIT') and (line != '.exit'):
            # filtering the input so that we only grab what we need
            line = line.replace(';', '')
            line_list = line.split(' ')

            # used to create database
            if line_list[0] == 'CREATE' and line_list[1] == 'DATABASE':
                # checks to make sure that the command had passed in a database name
                self.createDatabase(line_list)

            # used to create tables
            elif line_list[0] == 'create' and line_list[1] == 'table':
                self.createTable(current_directory, line)

            # used to delete databases
            elif line_list[0] == 'DROP' and line_list[1] == 'DATABASE':
                self.deleteDatabase(line_list)

            # used to delete tables
            elif line_list[0] == 'DROP' and line_list[1] == 'TABLE':
                self.removeTable(line_list, current_directory)

            # used to select which database we are using
            elif line_list[0] == 'USE' and DirectoryMgr.validateDir(line_list[1]):
                current_directory = line_list[1]
                print('Using ' + current_directory)

            # Selects header information from table
            elif (len(line_list) > 2 and (line_list[0] == 'SELECT' and line_list[1] == '*' and line_list[2] == 'FROM')) or (len(line_list) > 2 and line_list[0] == 'select' and line_list[1] == '*' and line_list[2] == 'from'):
                self.selectTable(line_list, current_directory)

            # inserting information into the tables
            elif line_list[0] == 'insert' and line_list[1] == 'into':
                try:
                    if len(current_directory) == 0:
                        print('Database is not selected')
                    else:
                        # parsing the information
                        first_parenth = line.index('(')
                        data = line[0: 0:] + line[first_parenth::]
                        data = ModifyCSV.removeOuterParentheses(data)
                        first_comma = data.index(',')
                        dataList = []
                        dataList.append(data[0:first_comma])
                        dataList.append(data[first_comma + 1:len(data)])

                        # attempt to insert the values
                        ModifyCSV.insertValues(line_list[2], current_directory, dataList)
                        print('Values Successfully inserted into ' + line_list[2])
                except:
                    if not DirectoryMgr.validateFile(line_list[2], current_directory):
                        print('Table does not exist')
                    else:
                        print('Error: problem inserting information')

            # deleting entries in tables
            elif line_list[0] == 'delete':
                try:
                    if len(current_directory) == 0:
                        print('Database is not selected')
                    else:
                        # while statement that doesn't break until the user uses a semicolon
                        while True:
                            # parsing input
                            new_input = input()
                            removed_semi_input = new_input
                            new_input_list = removed_semi_input.replace(';', '').split(' ')

                            # gets the column they want to delete from,
                            # what value they want,
                            # and the operator they want to use
                            if new_input_list[0] == 'where':
                                firstColumn = new_input_list[1]
                                deleteValue = new_input_list[3]
                                operator = new_input_list[2]
                            else:
                                print('Error: cannot read input')
                            if new_input.count(';') != 0:
                                break
                        # call specific functions based off of what operator they choose
                        if operator == '=':
                            ModifyCSV.deleteValuesEqual(line_list[2], current_directory, deleteValue, firstColumn)
                            print('Values successfully deleted')
                        elif operator == '>':
                            ModifyCSV.deleteValuesGreater(line_list[2], current_directory, deleteValue, firstColumn)
                            print('Values successfully deleted')
                        else:
                            print('Could not parse operator')
                except:
                    if not DirectoryMgr.validateFile(line_list[2], current_directory):
                        print('Table does not exist')
                    else:
                        print('Error: problem deleting information')

            # If user tries to commit while in the main for loop
            # we know that they haven't made any changes therefore we can abort
            elif line_list[0] == 'commit':
                print('Abort')

            else:
                print('Could not read input')

            line = input()

    def createDatabase(line_list):
        # checks to make sure that the command had passed in a database name
        if len(line_list) == 3:
            try:
                DirectoryMgr.makeDir(line_list[2])
                print('Database created successfully')
                return 1
            except:
                if DirectoryMgr.validateDir(line_list[2]):
                    print('Database already exists')
                else:
                    print('Database name is invalid')
                    return 0
        else:
            print('Error: No database name passed in')
            return 0

    def createTable(current_directory, line):
        try:
            # makes sure we are using a directory
            if len(current_directory) == 0:
                print('Database is not selected')
                return 0
            else:
                line = line.replace('(', '')
                line = line.replace(')', '')
                line = line.replace(',', '')
                line_data = line.split(' ')

                fileName = line_data[2]
                data = []
                data.append(line_data[3])
                data.append(line_data[4])
                data.append(line_data[5])
                data.append(line_data[6])
                data_dict = CSVHelper.Convert(data)

                ModifyCSV.writeHeaders(fileName, current_directory, data_dict)
                current_table = fileName
                print('Table created successfully')
                return 1
        except:
                return 0
            
    def deleteDatabase(line_list):
        # checks to make sure that the database name was passed in
        if len(line_list) == 3:
            try:
                DirectoryMgr.removeDir(line_list[2])
                print('Database removed successfully')
                return 1
            except:
                print('Database does not exist')
                return 0
        else:
            print('Error: No database name passed in')
            return 0

    def removeTable(line_list, current_directory):
        # checks to make sure that a file name was passed in
        if len(line_list) == 3:
            try:
                # makes sure we are using a directory
                if len(current_directory) == 0:
                    print('Database is not selected')
                    return 0
                else:
                    DirectoryMgr.removeFile(line_list[2], current_directory)
                    print('Table removed successfully')
                    return 1
            except:
                print('Table does not exist')
                return 0
        else:
            print('Error: No table name passed in')
            return 0

    def selectTable(line_list, current_directory):
        # makes sure that a table name was passed in
        if len(line_list) == 4:
            try:
                # makes sure we are using a directory
                if len(current_directory) == 0:
                    print('Database is not selected')
                    return 0
                else:
                    DirectoryMgr.readFile(line_list[3], current_directory)
                    return 1
            except:
                print('Error: problem reading file')
                return 0
        else:
            print('Error: No table name passed in')
            return 0
    