import openpyxl

wk=openpyxl.Workbook()
sh=wk.active
sh.title="Automation1"
print(sh.title)

sh['A3'].value="Selenium with Python"

#create another sheet in same file
sh1=wk.create_sheet(title="Automation2")
sh1=wk['Automation2']
sh1['A2']="Python"

# We can remove the sheet as well
wk.remove(wk["Automation1"])

wk.save("F:\Excel Automation\Pysheet.xlsx")