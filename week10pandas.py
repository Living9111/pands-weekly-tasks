import pandas as pd
import workbook as wb
listDAta= [
['John', 'math', 23],
['John', 'programming', 66],
['Mary', 'math', 45],
['Mary', 'programming', 33],
['Mark', 'SIEM', 57],
['Mark', 'programming', 70],
['Mark', 'math', 73],
['John', 'programming', 61]
]
df = pd.DataFrame(listDAta, columns=['name','subject','grade'])
print(df.head(3))

print(df.describe())
print(type(df.describe()))

mean = df.describe().loc['mean','grade']
print(mean)

# For CSV file
path = "c:/Users/MyPC/Desktop/week 1/week 2"
csvFilename = path + 'grades.csv'
df.to_csv(csvFilename)

# For Excel file
excelFilename = path +'grades.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')

with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
 df.describe().to_excel(writer, sheet_name="summary")


