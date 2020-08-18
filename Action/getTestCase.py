from PublicData.ProjectVar import *
from Utils.ParseExcel import ParseExcel

class HandleTestCase():

    def __init__(self,testFilePath):
        self.wb=ParseExcel()
        self.wb.loadWorkBook(testFilePath)

    def getTestAPIInfo(self,rowNum=None):
        #rowNum指定API的具体行
        #wb=ParseExcel()
        #wb.loadWorkBook(testFilePath)
        API_SheetObj=self.wb.getSheetByName("API")
        #print(API_SheetObj)

        testAPIAllInfo=self.wb.getRow(API_SheetObj,rowNum)
        print("testAPIAllInfo--->",testAPIAllInfo)
        APIName=testAPIAllInfo[1].value
        RequestUrl=testAPIAllInfo[2].value
        RequestMethod=testAPIAllInfo[3].value
        ParamsType=testAPIAllInfo[4].value
        CaseSheetName=testAPIAllInfo[5].value
        Active=testAPIAllInfo[6].value
        #print(APIName,RequestUrl,RequestMethod,ParamsType,CaseSheetName,Active)
        APIsheet_rows=self.wb.getRowsNumber(API_SheetObj)
        if Active=="y":
            testCaseSheetObj=self.wb.getSheetByName(CaseSheetName)
            print("testCaseSheetObj--->",testCaseSheetObj)
            testsheet_rows=self.wb.getRowsNumber(testCaseSheetObj)
            return testCaseSheetObj,APIName,RequestUrl, RequestMethod,ParamsType,CaseSheetName,Active,testsheet_rows,APIsheet_rows
        else:
            print("该接口%s,%s不用执行"%(APIName,CaseSheetName))

    def getTestCaseInfo(self,testCaseSheet,rowNum):
        #rowNum指定testcasesheet的具体行
        testCaseAllInfo=self.wb.getRow(testCaseSheet,rowNum)
        print("testCaseAllInfo--->",testCaseAllInfo)
        RequestData=testCaseAllInfo[0].value
        RelyData = testCaseAllInfo[1].value
        ResponseCode=testCaseAllInfo[2].value
        DataStore=testCaseAllInfo[4].value
        CheckPoint=testCaseAllInfo[5].value
        Active=testCaseAllInfo[6].value
        if Active=="y":
            #print(RequestData,RelyData,ResponseCode,DataStore,Active)
            return eval(RequestData),RelyData,ResponseCode,DataStore,eval(CheckPoint),Active
        else:
            print("[%s]第%s条用例不用执行"%(testCaseSheet.title,(rowNum-1)))
            return None

if  __name__=="__main__":
    hc=HandleTestCase(os.path.join(ProjectPath,"TestData\\testData.xlsx"))
    #print(hc.getTestAPIInfo(3))
    allinfo=hc.getTestAPIInfo(2)
    print("allifo",allinfo)
    if allinfo:
        testsheet=allinfo[0]
        print(hc.getTestCaseInfo(testsheet,2))