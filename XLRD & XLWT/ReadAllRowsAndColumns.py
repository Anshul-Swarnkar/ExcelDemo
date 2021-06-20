import xlrd

wk=xlrd.open_workbook("F:\Excel Automation\XLRD.xls")

ws=wk.sheet_by_name("Sheet1")
n=ws.nrows
c=ws.ncols

for i in range(0,n):
    for j in range(0,c):
        wc=ws.cell(i,j)
        print(wc.value)