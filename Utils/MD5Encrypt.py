from hashlib import md5


def md5_encrypt(str):
    md5_obj=md5()
    md5_obj.update(str.encode("utf-8"))
    md5_result=md5_obj.hexdigest()
    return md5_result

if __name__=="__main__":
    print(md5_encrypt("abc123"))

