import openpyxl

def export(headers,dataList,sheetname,excelname):
    wb=openpyxl.Workbook()
    sheet=wb.create_sheet(sheetname,0)
    sheet.append(headers)

    for data in dataList:
        sheet.append(data)

    wb.save(excelname+".xlsx")
