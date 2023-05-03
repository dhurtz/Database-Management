from ModifyCSV import ModifyCSV

deleteGreaterFile = 'deleteGreater'
database = 'testFolder'
value = '22'
column = 'Age'

output = ModifyCSV.deleteValuesGreater(deleteGreaterFile, database, value, column)
print(output)