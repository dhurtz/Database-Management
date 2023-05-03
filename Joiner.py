# Responsible for outer and inner joins
import os, csv
from CSVHelper import CSVHelper

class Joiner:
    def __init__(self) -> None:
        pass

    def outerJoin(first_tag, second_tag, first_table, second_table, database):
        # Initializing lists
        output_list = []
        used_list = []
        path_one = os.getcwd()
        path_one = path_one + '/' + database + '/' + first_table + '.csv'
        path_two = os.getcwd()
        path_two = path_two + '/' + database + '/' + second_table + '.csv'

        # get data from first file
        with open(path_one, 'r', newline='') as file_one:
            reader = csv.reader(file_one)
            data_1 = list(reader)
            file_one.close()

        # get data from second file
        with open(path_two, 'r', newline='') as file_two:
            reader = csv.reader(file_two)
            data_2 = list(reader)
            file_two.close()

        # find the column where their tags reside
        column_1 = CSVHelper.findColumn(data_1, first_tag)
        column_2 = CSVHelper.findColumn(data_2, second_tag)

        # add both the headers to the output
        output_list.append(data_1[0] + data_2[0])

        # Iterate through both lists,
        # if they have the same values in their respective columns,
        # then add them into our output,
        # add the first table to our used list so that we can tell later which variables didn't find a match
        for i in range(1, len(data_1)):
            for j in range(1, len(data_2)):
                if data_1[i][column_1] == data_2[j][column_2]:
                    output_list.append(data_1[i] + data_2[j])
                    used_list.append(data_1[i])

        # Iterate through them again,
        # if they aren't in the used list then we can add them to the file,
        # then add them to the used list as well
        for i in range(1, len(data_1)):
            if data_1[i] not in used_list:
                output_list.append(data_1[i])
                used_list.append(data_1[i])

        return output_list
    
    def innerJoin(first_tag, second_tag, first_table, second_table, database):
        # Initializing lists
        output_list = []

        # Creating paths
        path_one = os.getcwd()
        path_one = path_one + '/' + database + '/' + first_table + '.csv'
        path_two = os.getcwd()
        path_two = path_two + '/' + database + '/' + second_table + '.csv'

        # getting the data from the first file
        with open(path_one, 'r', newline='') as file_one:
            reader = csv.reader(file_one)
            data_1 = list(reader)
            file_one.close()

        # getting the data from the second file
        with open(path_two, 'r', newline='') as file_two:
            reader = csv.reader(file_two)
            data_2 = list(reader)
            file_two.close()

        # finding what columns these tags reside in
        column_1 = CSVHelper.findColumn(data_1, first_tag)
        column_2 = CSVHelper.findColumn(data_2, second_tag)

        # Adding the headers to the top of the output
        output_list.append(data_1[0] + data_2[0])

        # Iterate through both lists,
        # if they have the same values in their respective columns,
        # then add them into our output
        for i in range(len(data_1)):
            for j in range(len(data_2)):
                if data_1[i][column_1] == data_2[j][column_2]:
                    output_list.append(data_1[i] + data_2[j])

        return output_list
    
    def printJoin(self, first_tag, second_tag, first_table, second_table, join_type, database):
        if join_type == 'inner':
            output = self.innerJoin(first_tag, second_tag, first_table, second_table, database)
            CSVHelper.printList(output)
        elif join_type == 'outer':
            output = self.outerJoin(first_tag, second_tag, first_table, second_table, database)
            CSVHelper.printList(output)
        else:
            print('Error: invalid join type')
