from Utils.ParseExcel import ParseExcel


def writeResult(wb,sheetObj,errorinfo,response_data,result,rowNo):
    wb.writeCell(sheetObj,content=response_data,rowNo=rowNo,colsNo=4)
    print("4444444444444444444444444444")
    wb.writeCell(sheetObj, content=result, rowNo=rowNo, colsNo=8)
    print("555555555555555555555555555")
    if eval(errorinfo):
        wb.writeCell(sheetObj, content=errorinfo, rowNo=rowNo, colsNo=9)
    print("666666666666666666666666666")
    print("write down")


if __name__=="__main__":
    wb=ParseExcel()
    wb.loadWorkBook(r"E:\我的坚果云\framework\practice\excel_interface\TestData\testData.xlsx")
    ob=wb.getSheetByName("注册接口用例")
    writeResult(wb,ob, "{}", "{}","pass", 2)


