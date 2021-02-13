import xlrd
import docx
import pandas as pd

df = pd.read_csv("excel_tables.csv")
loc=("excel_tables.xlsx")
doc=docx.Document()

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(0, 0))