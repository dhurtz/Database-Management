# Responsible for any changes made to the tables in the database

import csv, os

class ModifyCSV:
    def __init__(self) -> None:
        pass

    # creates a file
    def writeHeaders(fileName, database, headers):
        new_row = []
        path = os.getcwd()
        path = path + '/' + database + '/' + fileName + '.csv'
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file)
            for key, value in headers.items():
                new_row.append(key + ' ' + value)
            writer.writerow(new_row)
            file.close()
            return 1

    # insert values into a table
    def insertValues(fileName, database, values):
        path = os.getcwd()
        path = path + '/' + database + '/' + fileName + '.csv'
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(values)
            file.close()
            return 1
    
        # reads data from a file
    def readFile(fileName, database):
        path = os.getcwd()
        path = path + '/' + database + '/' + fileName + '.csv'
        with open(path, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=' ', quotechar='|')
            for line in reader:
                print(' '.join(line))
            file.close()
        return 1

        # prints values that meets the requirements of the value not being equal too
    def readSpecificValuesNotEqual(fileName, database, firstColumn, secondColumn, thirdColumn, value):
        path = os.getcwd()
        path = path + '/' + database + '/' + fileName + '.csv'
        with open(path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            for i in range(len(data[0])):
                if data[0][i].count(firstColumn) > 0:
                    firstColumnNum = i
                elif data[0][i].count(secondColumn) > 0:
                    secondColumnNum = i
                elif data[0][i].count(thirdColumn) > 0:
                    thirdColumnNum = i
            for i in range(len(data)):
                if i != 0:
                    if float(data[i][firstColumnNum]) != float(value):
                        print(''.join(data[i][secondColumnNum] + ' ' + data[i][thirdColumnNum]))
                        return ''.join(data[i][secondColumnNum] + ' ' + data[i][thirdColumnNum])

    # changes a value to a new one when the columns are the same
    def changeValueWithSameColumn(fileName, database, oldValue, newValue):
        path = os.getcwd()
        path = path + '/' + database + '/' + fileName + '.csv'
        with open(path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            for i in range(len(data)):
                for j in range(len(data[i])):
                    if data[i][j] == oldValue:
                        data[i][j] = newValue
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return data

    # change a value to a new one when the columns are different
    def changeValueWithDifferentColumn(fileName, database, oldValue, newValue, columnName):
        path = os.getcwd()
        path = path + '/' + database + '/' + fileName + '.csv'
        with open(path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            for j in range(len(data[0])):
                if data[0][j].count(columnName) > 0:
                    ColumnNum = j
            for i in range(len(data)):
                for j in range(len(data[i])):
                    if data[i][j] == oldValue:
                        data[i][ColumnNum] = newValue
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return data

    
    # deletes rows that have elements equal to the value passed in
    def deleteValuesEqual(fileName, database, value, columnName):
        path = os.getcwd()
        path = path + '/' + database + '/' + fileName + '.csv'
        with open(path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            for i in range(len(data[0])):
                if data[0][i].count(columnName) > 0:
                    columnNum = i
            for i in reversed(range(len(data))):
                if data[i][columnNum] == value:
                    del(data[i])
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    
        # deletes rows that have elements greater than the value passed in
    def deleteValuesGreater(fileName, database, value, columnName):
        path = os.getcwd()
        path = path + '/' + database + '/' + fileName + '.csv'
        with open(path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            for i in range(len(data[0])):
                if data[0][i].count(columnName) > 0:
                    columnNum = i
            for i in reversed(range(len(data))):
                if i != 0:
                    if float(data[i][columnNum]) > float(value):
                        del(data[i])
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    # removes the outer parentheses from a string and returns it (This took too much time)
    def removeOuterParentheses(string):
        string_length = len(string)
        count_left, count_right = 0, 0
        res_list = list()
        left, right = None, None
        for i in range(string_length):
            if string[i] == '(':
                count_left += 1
                if count_left == 1:
                    left = i
            elif string[i] == ')':
                count_right += 1
                if count_right == count_left:
                    right = i
                    res_list.append(string[left + 1:right])
                    left, right = None, None
                    count_left, count_right = 0, 0
        return ''.join(res_list)
