#WRITE THE CONTENT IN XLS

from openpyxl import Workbook

wb = Workbook() # open spreadsheet
ws = wb.active # make it active
ws.append(['name','age'])
ws.append(['Sanjeev','21'])
wb.save('p1.xls')