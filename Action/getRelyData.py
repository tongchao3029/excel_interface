from PublicData.ProjectVar import *
from Utils.MD5Encrypt import md5_encrypt



#RelyData {"request":{"username":"register->1","password":"register->1"}}
#REQUEST_DATA {APIName:{"caseid":{"username":"","password":""}}}
#RESPONSE {APIName:{"caseid":{"userid":"","token":""}}}


def getRelyData(REQUEST_DATA,RESPONSE_DATA,RequestData,RelyData):
    for k,v in RelyData.items():
        if k=="request":
            for param,match in v.items():
                if param=="password":
                    RequestData[param]=md5_encrypt(REQUEST_DATA[match.split("->")[0]][match.split("->")[1]][param])
                else:
                    RequestData[param]=REQUEST_DATA[match.split("->")[0]][match.split("->")[1]][param]
        elif k=="response":
            for param,match in v.items():
                print(param,match)
                RequestData[param]=RESPONSE_DATA[match.split("->")[0]][match.split("->")[1]][param]
    print("RequestData",RequestData)
    return RequestData


if __name__=="__main__":
    getRelyData({'register': {'1': {'username': 'testman01', 'password': 'qwer12356'}}},{},{"username":"","password":""},{"request":{"username":"register->1","password":"register->1"}})
    getRelyData({'register': {'1': {'username': 'testman01', 'password': 'qwer12356'}}}, {"login":{"1":{"userid":"2","token":"ddddddd"}}}, {"userid":"","token":""}, {"response":{"userid":"login->1","token":"login->1"}})

