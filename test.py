from ModifyCSV import ModifyCSV

valuesNotEqualFile = 'changeColumn'
database = 'testFolder'
oldValue = '150'
newValue = '25'
columnName = 'Age'

output = ModifyCSV.changeValueWithDifferentColumn(valuesNotEqualFile, database, oldValue, newValue, columnName)
print(output)