from Action.getTestCase import HandleTestCase
from Utils.httpRequest import HttpRequest
from PublicData.ProjectVar import *
from Action.dataStore import dataStore
from Action.getRelyData import getRelyData
from Action.assertResult import assertResult
from Action.writeResult import writeResult
from Utils.ParseExcel import ParseExcel
from PublicData.getUniqnum import getUniqnum
import json


#testCaseSheetObj,APIName,RequestUrl, RequestMethod,ParamsType,CaseSheetName,Active
#RequestData,RelyData,ResponseCode,DataStore,Active
def main():
    wb = ParseExcel()
    wb.loadWorkBook(r"E:\framework\practice\excel_interface\TestData\testData.xlsx")
    hc = HandleTestCase(os.path.join(ProjectPath, "TestData\\testData.xlsx"))
    for i in range(2, 7): #需要算出api总表的行数
        allinfo = hc.getTestAPIInfo(i)
        if allinfo:
            testsheet = allinfo[0]
            #print(hc.getTestCaseInfo(testsheet, 2))
            APIName=allinfo[1]
            requestUrl=allinfo[2]
            requestMethod=allinfo[3]
            ParamsType=allinfo[4]
            testsheet_rows=allinfo[7]
        for j in range(2,testsheet_rows+1):
            #需要算出每个casesheet的行数
            sub=hc.getTestCaseInfo(testsheet, j)
            if sub:
                #eval(RequestData),RelyData,ResponseCode,DataStore,CheckPoint,Active
                print("sub",sub)
                hr = HttpRequest()
                RequestData=sub[0]
                if "username" in RequestData:
                    RequestData["username"]=RequestData["username"]+str(getUniqnum())
                RelyData=sub[1]
                ResponseCode=sub[2]
                DataStore=sub[3]
                CheckPoint=sub[4]
                if RelyData:
                    RequestData=getRelyData(REQUEST_DATA, RESPONSE_DATA, RequestData, eval(RelyData))
                    if APIName=="querycontent":
                        RequestData=str(RequestData[list(RequestData.keys())[0]])
                print(requestUrl, requestMethod, RequestData, ParamsType)
                response=hr.httpRequest(requestUrl, requestMethod, RequestData, ParamsType, cookies=None, headere=None)
                print("response",response.text)
                if DataStore:
                    print("dddddddddddddddddddddddddssssssss",RequestData)
                    dataStore(APIName,j-1,eval(DataStore),RequestData,json.loads(response.text))
                if response.status_code==ResponseCode:
                    assert_result=assertResult(json.loads(response.text),CheckPoint)
                    print("assert_reuslt",assert_result)
                else:
                    print("response_code不是200")
                print("assert_result[1]",str(assert_result[1]))
                #writeResult(hc.wb, testsheet, "{}", "{}", "pass", 2)
                writeResult(hc.wb,testsheet, str(assert_result[1]), str(response.text), "pass" if assert_result[0] else "fail",j)
                print("-"*100)
        print("REQUEST_DATA",REQUEST_DATA)
        print("RESPONSE_DATA",RESPONSE_DATA)




if __name__=="__main__":
   main()
