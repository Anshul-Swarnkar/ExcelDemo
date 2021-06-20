import xlwt

wk=xlwt.Workbook()
ws=wk.add_sheet("Automation")

ws.write(0,0,"Testing 1")
ws.write(0,1,"Testing 2")

wk.save("F:\Excel Automation\XLWT.xls")