import xlrd


# we need to create object of workbook
wk = xlrd.open_workbook("F:\Excel Automation\\XLRD.xls")

# found number of sheets
print(wk.nsheets)

# now we needd to move to sheet level

#ws= wk.sheet_by_index(0)
ws=wk.sheet_by_name("Sheet1")
print(ws.nrows)
print(ws.ncols)

#now move to cell level to pick data
wc=ws.cell(0,0)
print(wc.value)
