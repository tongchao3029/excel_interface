import json
import requests


class HttpRequest():
    def __init__(self):
        pass

    def httpRequest(self,requestUrl,requestMethod,requestData,ParamsType,cookies=None,headere=None):
        if requestMethod.lower()=="get":
            if ParamsType=="url":
               requestUrl="%s%s" %(requestUrl,requestData)
               response=self.__get(requestUrl)
               print("requestUrl",requestUrl)
               return response
            elif ParamsType=="data":
                response=self.__get(requestUrl,requestData)
                return response
        elif requestMethod.lower()=="post":
            if ParamsType=="data":
                response=self.__post(requestUrl,data=json.dumps(requestData))
                return response
            elif ParamsType=="json":
                response=self.__post(requestUrl,json=requestData)
                return response
        else:
            print("RequestMethod is not allowed")

    def __get(self,url, params=None,**kwargs):
        response=requests.get(url=url,params=params)
        return response

    def __post(self,url,data=None,json=None,**kwargs):
        response=requests.post(url=url,data=data,json=json)
        return response


if __name__ == "__main__":
    hr=HttpRequest()
    r=hr.httpRequest("http://39.106.41.11:8080/register/","POST",\
                                  {"username":"test333ddddd1","password":"qwer1dd234","email":"lily@qq.com"},"data")
    print(r.text)
    r2 = hr.httpRequest("http://39.106.41.11:8080/getBlogContent", "GET", \
                       "/1", "url")
    print(r2.text)