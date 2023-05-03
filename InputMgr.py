from DirectoryMgr import DirectoryMgr
from Joiner import Joiner
from CSVHelper import CSVHelper
from ModifyCSV import ModifyCSV
# Handles all the input from the user

class InputMgr:
    def __init__(self) -> None:
        pass

    def readInput():
        
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
                if len(line_list) == 3:
                    try:
                        DirectoryMgr.makeDir(line_list[2])
                        print('Database created successfully')
                    except:
                        if DirectoryMgr.validateDir(line_list[2]):
                            print('Database already exists')
                        else:
                            print('Database name is invalid')
                else:
                    print('Error: No database name passed in')

            # used to create tables
            elif line_list[0] == 'create' and line_list[1] == 'table':
                    try:
                        # makes sure we are using a directory
                        if len(current_directory) == 0:
                            print('Database is not selected')
                        else:
                            line = line.replace('(', '')
                            line = line.replace(')', '')
                            line = line.replace(',', '')
                            line_data = line.split(' ')
                            # fileName = findTableName(line_list[2])

                            # strips the parts of the string before the first (, removes the parenthesis, and makes it into a dict
                            # first_parenth = line.index('(')
                            # data = line[0: 0:] + line[first_parenth::]
                            # data = removeOuterParentheses(data)
                            # data = data.split(' ')
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
                    except:
                        if DirectoryMgr.validateFile(fileName, current_directory):
                            print('Table already exists')
                        else:
                            print('Table name is invalid')

            # used to delete databases
            elif line_list[0] == 'DROP' and line_list[1] == 'DATABASE':
                # checks to make sure that the database name was passed in
                if len(line_list) == 3:
                    try:
                        DirectoryMgr.removeDir(line_list[2])
                        print('Database removed successfully')
                    except:
                        print('Database does not exist')
                else:
                    print('Error: No database name passed in')

            # used to delete tables
            elif line_list[0] == 'DROP' and line_list[1] == 'TABLE':
                # checks to make sure that a file name was passed in
                if len(line_list) == 3:
                    try:
                        # makes sure we are using a directory
                        if len(current_directory) == 0:
                            print('Database is not selected')
                        else:
                            DirectoryMgr.removeFile(line_list[2], current_directory)
                            print('Table removed successfully')
                    except:
                        print('Table does not exist')
                else:
                    print('Error: No table name passed in')

            # used to select which database we are using
            elif line_list[0] == 'USE' and DirectoryMgr.validateDir(line_list[1]):
                current_directory = line_list[1]
                print('Using ' + current_directory)

            # Selects header information from table
            elif (len(line_list) > 2 and (line_list[0] == 'SELECT' and line_list[1] == '*' and line_list[2] == 'FROM')) or (len(line_list) > 2 and line_list[0] == 'select' and line_list[1] == '*' and line_list[2] == 'from'):
                # makes sure that a table name was passed in
                if len(line_list) == 4:
                    try:
                        # makes sure we are using a directory
                        if len(current_directory) == 0:
                            print('Database is not selected')
                        else:
                            DirectoryMgr.readFile(line_list[3], current_directory)
                            current_table = line_list[3]
                    except:
                        print('Error: problem reading file')
                else:
                    print('Error: No table name passed in')
            elif line_list[0] == 'select' and line_list[1] == '*':
                try:
                    if len(current_directory) == 0:
                        print('Database is not selected')
                    else:
                        while True:
                            new_input = input()
                            new_input_list = new_input.replace(';', '').split(' ')

                            # then we know they are entering in which tags they'd like to use
                            if len(new_input_list) == 4:
                                first_tag = new_input_list[1]
                                second_tag = new_input_list[3]

                                first_tag_index = first_tag.index('.')
                                second_tag_index = second_tag.index('.')

                                # parsing what tags they want via finding the periods and taking the string after that
                                first_tag_parsed = first_tag[first_tag_index + 1:len(first_tag)]
                                second_tag_parsed = second_tag[second_tag_index + 1:len(second_tag)]

                                Joiner.printJoin(first_tag_parsed, second_tag_parsed, first_table, second_table, join_type, current_directory)

                            # Then we know that they are using the short hand for the inner join
                            elif len(new_input_list) == 5:
                                first_table = new_input_list[1]
                                second_table = new_input_list[3]
                                join_type = 'inner'

                            # they aren't specifying which side so we know  it's an inner join
                            elif len(new_input_list) == 7:
                                first_table = new_input_list[1]
                                second_table = new_input_list[5]
                                join_type = 'inner'

                            # we know that it's outer because they must be specifying which side they'd like
                            elif len(new_input_list) == 8:
                                first_table = new_input_list[1]
                                second_table = new_input_list[6]
                                join_type = 'outer'

                            # break us out of this input with a semi colon
                            if new_input.count(';') > 0:
                                break
                except:
                    print('Error reading file')

            # for selecting specific columns to print out
            elif line_list[0] == 'select':
                try:
                    if len(current_directory) == 0:
                        print('Database is not selected')
                    else:
                        # loop to contain the commands that don't have semicolons
                        while True:
                            # parsing the new inputs
                            new_input = input()
                            removed_semi_input = new_input
                            new_input_list = removed_semi_input.replace(';', '').split(' ')

                            # getting the columns that the user wanted to print out
                            secondColumn = line_list[1]
                            thirdColumn = line_list[2]
                            secondColumn.replace(',','')

                            # getting which table they'd like
                            if new_input_list[0] == 'from':
                                table = new_input_list[1]

                            # what condition they want to print it off of
                            elif new_input_list[0] == 'where':
                                firstColumn = new_input_list[1]
                                if new_input_list[2] == '!=':
                                    value = new_input_list[3]

                            # break the loop if we have a semicolon in the command
                            if new_input.count(';') > 0:
                                break
                        # after the statement is broken we attempt to print out the values
                        ModifyCSV.readSpecificValuesNotEqual(table, current_directory, firstColumn, secondColumn, thirdColumn, value)
                except:
                    print('Error: problem reading file')
            # Adds data to a table
            elif line_list[0] == 'ALTER' and line_list[1] == 'TABLE' and line_list[3] == 'ADD':
                try:
                    if len(current_directory) == 0:
                        print('Database is not selected')
                    else:
                        # strips the parts of the string before the first (, removes the parenthesis, and makes it into a list
                        data = [line_list[4], line_list[5]]
                        # we convert the data into key pair so that we can write it to the csv files
                        data_dict = CSVHelper.Convert(data)
                        ModifyCSV.writeHeaders(line_list[2], current_directory, data_dict)
                        print('Table ' + line_list[2] + ' modified.')
                except:
                    print('Error: problem reading file')
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
            # updating different parts of the tables
            elif line_list[0] == 'update' and len(line_list) == 0:
                try:
                    if len(current_directory) == 0:
                        print('Database is not selected')
                    else:
                        # while statement that doesn't break until the user uses a semicolon
                        while True:
                            # parsing the input
                            new_input = input()
                            removed_semi_input = new_input
                            new_input_list = removed_semi_input.replace(';', '').split(' ')

                            # getting the column they want to change and the value they want to change it too
                            if new_input_list[0] == 'set':
                                firstColumn = new_input_list[1]
                                newValue = new_input_list[3]
                            # getting the second column to identify what data they want to change with the old value
                            elif new_input_list[0] == 'where':
                                secondColumn = new_input_list[1]
                                oldValue = new_input_list[3]
                            else:
                                print('Error: cannot read input')
                            if new_input.count(';') != 0:
                                break
                        # if the columns are the same we can use a specific function to change those values
                        if firstColumn == secondColumn:
                            ModifyCSV.changeValueWithSameColumn(line_list[1], current_directory, oldValue, newValue)
                        # if the columns are different we will want to use a different approach
                        elif firstColumn != secondColumn:
                            ModifyCSV.changeValueWithDifferentColumn(line_list[1], current_directory, oldValue, newValue, firstColumn)

                        print('Value successfully changed')
                except:
                    if not DirectoryMgr.validateFile(line_list[1], current_directory):
                        print('Table does not exist')
                    else:
                        print('Error: problem altering information')
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
