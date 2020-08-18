import re

#{"code":"00","userid":{"type":"int","value":"^\d+$"}}


def assertResult(response_data,CheckPoint):
    error_info={}
    for k,v in CheckPoint.items():
        if k in response_data:
            if isinstance(CheckPoint[k],str):
                print(response_data)
                print(CheckPoint[k])
                print(response_data[k])
                if CheckPoint[k]!=response_data[k]:
                    error_info[k]=response_data[k]
            elif isinstance(CheckPoint[k],dict):
                for i in CheckPoint[k].keys():
                    if i=="type":
                        if not isinstance(response_data[k],eval(CheckPoint[k][i])):
                            if k not in error_info:
                                error_info[k] = {i: str(type(response_data[k]))}
                            else:
                                if i not in error_info[k]:
                                    error_info[k] = {i:str(type(response_data[k]))}
                                else:
                                    error_info[k][i]=str(type(response_data[k]))
                    elif i=="value":
                        regx=CheckPoint[k][i]
                        print("regx",regx)
                        if not re.search(regx,str(response_data[k])):
                            if k not in error_info:
                                error_info[k]={i:"not match"}
                            else:
                                error_info[k][i]="not match"
        else:
            print("响应结果中不存在[%s]"%k)
    if error_info:
        return False,error_info
    return True,error_info


if __name__=="__main__":
    print(assertResult({"userid": "f32", "code": "012"},{"code":"00","userid":{"type":"int","value":"^\d+$"}}))
    print(assertResult({"userid": "32", "code": "00"}, {"code": "00", "userid": {"type": "int", "value": "^\d+$"}}))