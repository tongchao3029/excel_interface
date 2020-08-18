from PublicData.ProjectVar import REQUEST_DATA,RESPONSE_DATA
#REQUEST_DATA {APIName:{"caseid":{"username":"","password":""}}}
#RESPONSE {APIName:{"caseid":{"userid":"","token":""}}}
#store_point {"request":["username","password"],"response":["code"]}

def dataStore(APIName,caseid,store_point,request_data,response_data):
    for k,v in store_point.items():
        print(k,v)
        if k=="request":
            for i in v:
                if i in request_data:
                    if APIName not in REQUEST_DATA:
                        REQUEST_DATA[APIName]={str(caseid):{i:request_data[i]}}
                    else:
                        if str(caseid) not in REQUEST_DATA[APIName]:
                            REQUEST_DATA[APIName][str(caseid)] ={i:request_data[i]}
                        else:
                            REQUEST_DATA[APIName][str(caseid)][i]=request_data[i]
                else:
                    print("请求参数中不含[%s]字段"%i)
        elif k=="response":
            for j in v:
                if j in str(response_data):
                    if j !="articleId":
                        if APIName not in RESPONSE_DATA:
                            RESPONSE_DATA[APIName]={str(caseid):{j:response_data[j]}}
                        else:
                            if str(caseid) not in RESPONSE_DATA[APIName]:
                                RESPONSE_DATA[APIName][str(caseid)]={j:response_data[j]}
                            else:
                                RESPONSE_DATA[APIName][str(caseid)][j]=response_data[j]
                    elif j =="articleId":
                        if APIName not in RESPONSE_DATA:
                            print("xxxxxxxxxxxxxxxxxxx",response_data["data"][0])
                            RESPONSE_DATA[APIName]={str(caseid):{j:response_data["data"][0][j]}}
                        else:
                            if str(caseid) not in RESPONSE_DATA[APIName]:
                                RESPONSE_DATA[APIName][str(caseid)]={j:response_data["data"][0][j]}
                            else:
                                RESPONSE_DATA[APIName][str(caseid)][j]=response_data["data"][0][j]
                else:
                    print("响应参数中不含[%s]字段"%j)
        print("####stored %s'data done###"%k)


if __name__=="__main__":
    dataStore("register",3,{"request":["username","password"],"response":["code"]},\
              {"username":"test","password":"qwer1234","email":"lily@qq.com"},{"username":"test","password":"qwer1234","email":"lily@qq.com"})
    dataStore("login", 3, {"response":["userid","token"]},{"username":"test","password":"qwer1234","email":"lily@qq.com"},{"token": "a58a28896d1ac2cb6bc7b3c79f8202a2", "code": "00", "userid": 285, "login_time": "2020-06-11 16:43:40"})

    print("REQUEST_DATA",REQUEST_DATA)
    print("RESPONSE_DATA",RESPONSE_DATA)
