# Helper methods for looking through csv files

class CSVHelper:
    def __init__(self) -> None:
        pass

    # finds what row that the value is in
    def findColumn(data, value):
        for row in data:
            for column, v in enumerate(row):
                if v.count(value) > 0:
                    return column
    
    def printList(list):
        for line in list:
            for word in line:
                print(word + '|', end='')
            print('')

    # Converts a list into a dictionary
    def Convert(list):
        result_dct = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
        return result_dct


    def findTableName(line):
        first_parenth = line.index('(')
        newString = line[0:first_parenth]
        return newString