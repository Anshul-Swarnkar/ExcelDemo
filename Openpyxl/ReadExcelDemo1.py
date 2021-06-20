import openpyxl

wk=openpyxl.load_workbook("F:\Excel Automation\ReadExcel.xlsx")

print(wk.sheetnames)
print("Active Sheet is " + wk.active.title)

sh=wk["Members"]
print(sh.title) 