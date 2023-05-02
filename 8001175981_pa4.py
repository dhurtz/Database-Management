# Dustin Hurtz
# 10/10/22
# CS 457

import os, csv
# from filelock import FileLock
from InputMgr import InputMgr

# Reads input from the user
# def readInput():
#     print('Please Enter a command \n'
#           'Enter .EXIT to close program')
#     line = input()
#     current_directory = ''
#     while (line != '.EXIT') and (line != '.exit'):
#         # filtering the input so that we only grab what we need
#         line = line.replace(';', '')
#         line_list = line.split(' ')

#         # used to create database
#         if line_list[0] == 'CREATE' and line_list[1] == 'DATABASE':
#             # checks to make sure that the command had passed in a database name
#             if len(line_list) == 3:
#                 try:
#                     makeDir(line_list[2])
#                     print('Database created successfully')
#                 except:
#                     if validateDir(line_list[2]):
#                         print('Database already exists')
#                     else:
#                         print('Database name is invalid')
#             else:
#                 print('Error: No database name passed in')

#         # used to create tables
#         elif line_list[0] == 'create' and line_list[1] == 'table':
#                 try:
#                     # makes sure we are using a directory
#                     if len(current_directory) == 0:
#                         print('Database is not selected')
#                     else:
#                         line = line.replace('(', '')
#                         line = line.replace(')', '')
#                         line = line.replace(',', '')
#                         line_data = line.split(' ')
#                         # fileName = findTableName(line_list[2])

#                         # strips the parts of the string before the first (, removes the parenthesis, and makes it into a dict
#                         # first_parenth = line.index('(')
#                         # data = line[0: 0:] + line[first_parenth::]
#                         # data = removeOuterParentheses(data)
#                         # data = data.split(' ')
#                         fileName = line_data[2]
#                         data = []
#                         data.append(line_data[3])
#                         data.append(line_data[4])
#                         data.append(line_data[5])
#                         data.append(line_data[6])
#                         data_dict = Convert(data)

#                         writeHeaders(fileName, current_directory, data_dict)
#                         current_table = fileName
#                         print('Table created successfully')
#                 except:
#                     if validateFile(fileName, current_directory):
#                         print('Table already exists')
#                     else:
#                         print('Table name is invalid')

#         # used to delete databases
#         elif line_list[0] == 'DROP' and line_list[1] == 'DATABASE':
#             # checks to make sure that the database name was passed in
#             if len(line_list) == 3:
#                 try:
#                     removeDir(line_list[2])
#                     print('Database removed successfully')
#                 except:
#                     print('Database does not exist')
#             else:
#                 print('Error: No database name passed in')

#         # used to delete tables
#         elif line_list[0] == 'DROP' and line_list[1] == 'TABLE':
#             # checks to make sure that a file name was passed in
#             if len(line_list) == 3:
#                 try:
#                     # makes sure we are using a directory
#                     if len(current_directory) == 0:
#                         print('Database is not selected')
#                     else:
#                         removeFile(line_list[2], current_directory)
#                         print('Table removed successfully')
#                 except:
#                     print('Table does not exist')
#             else:
#                 print('Error: No table name passed in')

#         # used to select which database we are using
#         elif line_list[0] == 'USE' and validateDir(line_list[1]):
#             current_directory = line_list[1]
#             print('Using ' + current_directory)

#         # Selects header information from table
#         elif (len(line_list) > 2 and (line_list[0] == 'SELECT' and line_list[1] == '*' and line_list[2] == 'FROM')) or (len(line_list) > 2 and line_list[0] == 'select' and line_list[1] == '*' and line_list[2] == 'from'):
#             # makes sure that a table name was passed in
#             if len(line_list) == 4:
#                 try:
#                     # makes sure we are using a directory
#                     if len(current_directory) == 0:
#                         print('Database is not selected')
#                     else:
#                         readFile(line_list[3], current_directory)
#                         current_table = line_list[3]
#                 except:
#                     print('Error: problem reading file')
#             else:
#                 print('Error: No table name passed in')
#         elif line_list[0] == 'select' and line_list[1] == '*':
#             try:
#                 if len(current_directory) == 0:
#                     print('Database is not selected')
#                 else:
#                     while True:
#                         new_input = input()
#                         new_input_list = new_input.replace(';', '').split(' ')

#                         # then we know they are entering in which tags they'd like to use
#                         if len(new_input_list) == 4:
#                             first_tag = new_input_list[1]
#                             second_tag = new_input_list[3]

#                             first_tag_index = first_tag.index('.')
#                             second_tag_index = second_tag.index('.')

#                             # parsing what tags they want via finding the periods and taking the string after that
#                             first_tag_parsed = first_tag[first_tag_index + 1:len(first_tag)]
#                             second_tag_parsed = second_tag[second_tag_index + 1:len(second_tag)]

#                             printJoin(first_tag_parsed, second_tag_parsed, first_table, second_table, join_type, current_directory)

#                         # Then we know that they are using the short hand for the inner join
#                         elif len(new_input_list) == 5:
#                             first_table = new_input_list[1]
#                             second_table = new_input_list[3]
#                             join_type = 'inner'

#                         # they aren't specifying which side so we know  it's an inner join
#                         elif len(new_input_list) == 7:
#                             first_table = new_input_list[1]
#                             second_table = new_input_list[5]
#                             join_type = 'inner'

#                         # we know that it's outer because they must be specifying which side they'd like
#                         elif len(new_input_list) == 8:
#                             first_table = new_input_list[1]
#                             second_table = new_input_list[6]
#                             join_type = 'outer'

#                         # break us out of this input with a semi colon
#                         if new_input.count(';') > 0:
#                             break
#             except:
#                 print('Error reading file')

#         # for selecting specific columns to print out
#         elif line_list[0] == 'select':
#             try:
#                 if len(current_directory) == 0:
#                     print('Database is not selected')
#                 else:
#                     # loop to contain the commands that don't have semicolons
#                     while True:
#                         # parsing the new inputs
#                         new_input = input()
#                         removed_semi_input = new_input
#                         new_input_list = removed_semi_input.replace(';', '').split(' ')

#                         # getting the columns that the user wanted to print out
#                         secondColumn = line_list[1]
#                         thirdColumn = line_list[2]
#                         secondColumn.replace(',','')

#                         # getting which table they'd like
#                         if new_input_list[0] == 'from':
#                             table = new_input_list[1]

#                         # what condition they want to print it off of
#                         elif new_input_list[0] == 'where':
#                             firstColumn = new_input_list[1]
#                             if new_input_list[2] == '!=':
#                                 value = new_input_list[3]

#                         # break the loop if we have a semicolon in the command
#                         if new_input.count(';') > 0:
#                             break
#                     # after the statement is broken we attempt to print out the values
#                     readSpecificValuesNotEqual(table, current_directory, firstColumn, secondColumn, thirdColumn, value)
#             except:
#                 print('Error: problem reading file')
#         # Adds data to a table
#         elif line_list[0] == 'ALTER' and line_list[1] == 'TABLE' and line_list[3] == 'ADD':
#             try:
#                 if len(current_directory) == 0:
#                     print('Database is not selected')
#                 else:
#                     # strips the parts of the string before the first (, removes the parenthesis, and makes it into a list
#                     data = [line_list[4], line_list[5]]
#                     # we convert the data into key pair so that we can write it to the csv files
#                     data_dict = Convert(data)
#                     writeHeaders(line_list[2], current_directory, data_dict)
#                     print('Table ' + line_list[2] + ' modified.')
#             except:
#                 print('Error: problem reading file')
#         # inserting information into the tables
#         elif line_list[0] == 'insert' and line_list[1] == 'into':
#             try:
#                 if len(current_directory) == 0:
#                     print('Database is not selected')
#                 else:
#                     # parsing the information
#                     first_parenth = line.index('(')
#                     data = line[0: 0:] + line[first_parenth::]
#                     data = removeOuterParentheses(data)
#                     first_comma = data.index(',')
#                     dataList = []
#                     dataList.append(data[0:first_comma])
#                     dataList.append(data[first_comma + 1:len(data)])

#                     # attempt to insert the values
#                     insertValues(line_list[2], current_directory, dataList)
#                     print('Values Successfully inserted into ' + line_list[2])
#             except:
#                 if not validateFile(line_list[2], current_directory):
#                     print('Table does not exist')
#                 else:
#                     print('Error: problem inserting information')
#         # updating different parts of the tables
#         elif line_list[0] == 'update' and len(line_list) == 0:
#             try:
#                 if len(current_directory) == 0:
#                     print('Database is not selected')
#                 else:
#                     # while statement that doesn't break until the user uses a semicolon
#                     while True:
#                         # parsing the input
#                         new_input = input()
#                         removed_semi_input = new_input
#                         new_input_list = removed_semi_input.replace(';', '').split(' ')

#                         # getting the column they want to change and the value they want to change it too
#                         if new_input_list[0] == 'set':
#                             firstColumn = new_input_list[1]
#                             newValue = new_input_list[3]
#                         # getting the second column to identify what data they want to change with the old value
#                         elif new_input_list[0] == 'where':
#                             secondColumn = new_input_list[1]
#                             oldValue = new_input_list[3]
#                         else:
#                             print('Error: cannot read input')
#                         if new_input.count(';') != 0:
#                             break
#                     # if the columns are the same we can use a specific function to change those values
#                     if firstColumn == secondColumn:
#                         changeValueWithSameColumn(line_list[1], current_directory, oldValue, newValue)
#                     # if the columns are different we will want to use a different approach
#                     elif firstColumn != secondColumn:
#                         changeValueWithDifferentColumn(line_list[1], current_directory, oldValue, newValue, firstColumn)

#                     print('Value successfully changed')
#             except:
#                 if not validateFile(line_list[1], current_directory):
#                     print('Table does not exist')
#                 else:
#                     print('Error: problem altering information')
#         # deleting entries in tables
#         elif line_list[0] == 'delete':
#             try:
#                 if len(current_directory) == 0:
#                     print('Database is not selected')
#                 else:
#                     # while statement that doesn't break until the user uses a semicolon
#                     while True:
#                         # parsing input
#                         new_input = input()
#                         removed_semi_input = new_input
#                         new_input_list = removed_semi_input.replace(';', '').split(' ')

#                         # gets the column they want to delete from,
#                         # what value they want,
#                         # and the operator they want to use
#                         if new_input_list[0] == 'where':
#                             firstColumn = new_input_list[1]
#                             deleteValue = new_input_list[3]
#                             operator = new_input_list[2]
#                         else:
#                             print('Error: cannot read input')
#                         if new_input.count(';') != 0:
#                             break
#                     # call specific functions based off of what operator they choose
#                     if operator == '=':
#                         deleteValuesEqual(line_list[2], current_directory, deleteValue, firstColumn)
#                         print('Values successfully deleted')
#                     elif operator == '>':
#                         deleteValuesGreater(line_list[2], current_directory, deleteValue, firstColumn)
#                         print('Values successfully deleted')
#                     else:
#                         print('Could not parse operator')
#             except:
#                 if not validateFile(line_list[2], current_directory):
#                     print('Table does not exist')
#                 else:
#                     print('Error: problem deleting information')

#         elif line_list[0] == 'begin' and line_list[1] == 'transaction':
#             # locking file
#             lock = FileLock(current_table + '.lock')
#             try:
#                 # acquiring lock,
#                 # if it takes 5 seconds we can assume that we can't access it and return the user to the main state
#                 lock.acquire(timeout=5)
#                 with lock:
#                     print('Transaction starts.')
#                     # while the user hasn't committed their changes
#                     while True:
#                         new_input = input()
#                         new_input_list = new_input.replace(';', '').split(' ')
#                         if new_input_list[0] == 'commit':
#                             lock.release()
#                             print('Changes Committed')
#                             break
#                         # we can update the table
#                         elif new_input_list[0] == 'update':
#                             first_header = new_input_list[3]
#                             second_header = new_input_list[7]
#                             first_value = new_input_list[5]
#                             second_value = new_input_list[9]
#                             try:
#                                 changeValueWithDifferentColumn(current_table, current_directory,
#                                                             second_value, first_value, first_header)
#                                 print('File Updated')
#                             except:
#                                 print('Error: Cannot update file')
#             except:
#                 print('Error: file is already locked')

#         # If user tries to commit while in the main for loop
#         # we know that they haven't made any changes therefore we can abort
#         elif line_list[0] == 'commit':
#             print('Abort')

#         else:
#             print('Could not read input')

#         line = input()


# # validates if a directory exists
# def validateDir(dirName):
#     path = os.getcwd()
#     path = path + '/' + dirName
#     return os.path.isdir(path)


# # creates a directory
# def makeDir(dirName):
#     path = os.getcwd()
#     path = path + '/' + dirName
#     return os.mkdir(path)


# # removes a directory
# def removeDir(dirName):
#     path = os.getcwd()
#     path = path + '/' + dirName
#     return os.rmdir(path)


# # validates if a file exists
# def validateFile(fileName, database):
#     path = os.getcwd()
#     path = path + '/' + database + '/' + fileName + '.csv'
#     return os.path.isfile(path)


# # creates a file
# def writeHeaders(fileName, database, headers):
#     new_row = []
#     path = os.getcwd()
#     path = path + '/' + database + '/' + fileName + '.csv'
#     with open(path, 'a', newline='') as file:
#         writer = csv.writer(file)
#         for key, value in headers.items():
#             new_row.append(key + ' ' + value)
#         writer.writerow(new_row)
#         file.close()


# # insert values into a table
# def insertValues(fileName, database, values):
#     path = os.getcwd()
#     path = path + '/' + database + '/' + fileName + '.csv'
#     with open(path, 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(values)
#         file.close()


# # removes a file
# def removeFile(fileName, database):
#     path = os.getcwd()
#     path = path + '/' + database + '/' + fileName + '.csv'
#     return os.remove(path)


# # reads data from a file
# def readFile(fileName, database):
#     path = os.getcwd()
#     path = path + '/' + database + '/' + fileName + '.csv'
#     with open(path, 'r', newline='') as file:
#         reader = csv.reader(file, delimiter=' ', quotechar='|')
#         for line in reader:
#             print(' '.join(line))
#         file.close()


# # prints values that meets the requirements of the value not being equal too
# def readSpecificValuesNotEqual(fileName, database, firstColumn, secondColumn, thirdColumn, value):
#     path = os.getcwd()
#     path = path + '/' + database + '/' + fileName + '.csv'
#     with open(path, 'r', newline='') as file:
#         reader = csv.reader(file)
#         data = list(reader)
#         for i in range(len(data[0])):
#             if data[0][i].count(firstColumn) > 0:
#                 firstColumnNum = i
#             elif data[0][i].count(secondColumn) > 0:
#                 secondColumnNum = i
#             elif data[0][i].count(thirdColumn) > 0:
#                 thirdColumnNum = i
#         for i in range(len(data)):
#             if i != 0:
#                 if float(data[i][firstColumnNum]) != float(value):
#                     print(''.join(data[i][secondColumnNum] + ' ' + data[i][thirdColumnNum]))


# # finds what row that the value is in
# def findColumn(data, value):
#     for row in data:
#         for column, v in enumerate(row):
#             if v.count(value) > 0:
#                 return column

# need to find column index, then search that column for the old value. And replace with the new value


# # changes a value to a new one when the columns are the same
# def changeValueWithSameColumn(fileName, database, oldValue, newValue):
#     path = os.getcwd()
#     path = path + '/' + database + '/' + fileName + '.csv'
#     with open(path, 'r', newline='') as file:
#         reader = csv.reader(file)
#         data = list(reader)
#         for i in range(len(data)):
#             for j in range(len(data[i])):
#                 if data[i][j] == oldValue:
#                     data[i][j] = newValue
#     with open(path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)


# # change a value to a new one when the columns are different
# def changeValueWithDifferentColumn(fileName, database, oldValue, newValue, columnName):
#     path = os.getcwd()
#     path = path + '/' + database + '/' + fileName + '.csv'
#     with open(path, 'r', newline='') as file:
#         reader = csv.reader(file)
#         data = list(reader)
#         for j in range(len(data[0])):
#             if data[0][j].count(columnName) > 0:
#                 ColumnNum = j
#         for i in range(len(data)):
#             for j in range(len(data[i])):
#                 if data[i][j] == oldValue:
#                     data[i][ColumnNum] = newValue
#     with open(path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)


# # deletes rows that have elements equal to the value passed in
# def deleteValuesEqual(fileName, database, value, columnName):
#     path = os.getcwd()
#     path = path + '/' + database + '/' + fileName + '.csv'
#     with open(path, 'r', newline='') as file:
#         reader = csv.reader(file)
#         data = list(reader)
#         for i in range(len(data[0])):
#             if data[0][i].count(columnName) > 0:
#                 columnNum = i
#         for i in reversed(range(len(data))):
#             if data[i][columnNum] == value:
#                 del(data[i])
#     with open(path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)


# # deletes rows that have elements greater than the value passed in
# def deleteValuesGreater(fileName, database, value, columnName):
#     path = os.getcwd()
#     path = path + '/' + database + '/' + fileName + '.csv'
#     with open(path, 'r', newline='') as file:
#         reader = csv.reader(file)
#         data = list(reader)
#         for i in range(len(data[0])):
#             if data[0][i].count(columnName) > 0:
#                 columnNum = i
#         for i in reversed(range(len(data))):
#             if i != 0:
#                 if float(data[i][columnNum]) > float(value):
#                     del(data[i])
#     with open(path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)


# # removes the outer parentheses from a string and returns it (This took too much time)
# def removeOuterParentheses(string):
#     string_length = len(string)
#     count_left, count_right = 0, 0
#     res_list = list()
#     left, right = None, None
#     for i in range(string_length):
#         if string[i] == '(':
#             count_left += 1
#             if count_left == 1:
#                 left = i
#         elif string[i] == ')':
#             count_right += 1
#             if count_right == count_left:
#                 right = i
#                 res_list.append(string[left + 1:right])
#                 left, right = None, None
#                 count_left, count_right = 0, 0
#     return ''.join(res_list)


# # Converts a list into a dictionary
# def Convert(list):
#     result_dct = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
#     return result_dct


# def findTableName(line):
#     first_parenth = line.index('(')
#     newString = line[0:first_parenth]
#     return newString


# def printJoin(first_tag, second_tag, first_table, second_table, join_type, database):
#     if join_type == 'inner':
#         output = innerJoin(first_tag, second_tag, first_table, second_table, database)
#         printList(output)
#     elif join_type == 'outer':
#         output = outerJoin(first_tag, second_tag, first_table, second_table, database)
#         printList(output)
#     else:
#         print('Error: invalid join type')


# def innerJoin(first_tag, second_tag, first_table, second_table, database):
#     # Initializing lists
#     line_list_1 = []
#     line_list_2 = []
#     output_list = []

#     # Creating paths
#     path_one = os.getcwd()
#     path_one = path_one + '/' + database + '/' + first_table + '.csv'
#     path_two = os.getcwd()
#     path_two = path_two + '/' + database + '/' + second_table + '.csv'

#     # getting the data from the first file
#     with open(path_one, 'r', newline='') as file_one:
#         reader = csv.reader(file_one)
#         data_1 = list(reader)
#         file_one.close()

#     # getting the data from the second file
#     with open(path_two, 'r', newline='') as file_two:
#         reader = csv.reader(file_two)
#         data_2 = list(reader)
#         file_two.close()

#     # finding what columns these tags reside in
#     column_1 = findColumn(data_1, first_tag)
#     column_2 = findColumn(data_2, second_tag)

#     # Adding the headers to the top of the output
#     output_list.append(data_1[0] + data_2[0])

#     # Iterate through both lists,
#     # if they have the same values in their respective columns,
#     # then add them into our output
#     for i in range(len(data_1)):
#         for j in range(len(data_2)):
#             if data_1[i][column_1] == data_2[j][column_2]:
#                 output_list.append(data_1[i] + data_2[j])

#     return output_list


# def outerJoin(first_tag, second_tag, first_table, second_table, database):
#     # Initializing lists
#     output_list = []
#     used_list = []
#     path_one = os.getcwd()
#     path_one = path_one + '/' + database + '/' + first_table + '.csv'
#     path_two = os.getcwd()
#     path_two = path_two + '/' + database + '/' + second_table + '.csv'

#     # get data from first file
#     with open(path_one, 'r', newline='') as file_one:
#         reader = csv.reader(file_one)
#         data_1 = list(reader)
#         file_one.close()

#     # get data from second file
#     with open(path_two, 'r', newline='') as file_two:
#         reader = csv.reader(file_two)
#         data_2 = list(reader)
#         file_two.close()

#     # find the column where their tags reside
#     column_1 = findColumn(data_1, first_tag)
#     column_2 = findColumn(data_2, second_tag)

#     # add both the headers to the output
#     output_list.append(data_1[0] + data_2[0])

#     # Iterate through both lists,
#     # if they have the same values in their respective columns,
#     # then add them into our output,
#     # add the first table to our used list so that we can tell later which variables didn't find a match
#     for i in range(1, len(data_1)):
#         for j in range(1, len(data_2)):
#             if data_1[i][column_1] == data_2[j][column_2]:
#                 output_list.append(data_1[i] + data_2[j])
#                 used_list.append(data_1[i])

#     # Iterate through them again,
#     # if they aren't in the used list then we can add them to the file,
#     # then add them to the used list as well
#     for i in range(1, len(data_1)):
#         if data_1[i] not in used_list:
#             output_list.append(data_1[i])
#             used_list.append(data_1[i])

#     return output_list


# def printList(list):
#     for line in list:
#         for word in line:
#             print(word + '|', end='')
#         print('')

# calls our input function
def main():
    InputMgr.readInput()


# running main
if __name__ == "__main__":
    main()


# itterate through both of the arrays at the same time.
# we want to find what row has the tags in it
# only use that row to print out what things we want into the two lists