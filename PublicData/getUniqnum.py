from PublicData.ProjectVar import ProjectPath
import os




def getUniqnum():
    with open(os.path.join(ProjectPath,"PublicData\\uniquenumber"),"r+") as fp:
        number=fp.read()
        new_number=int(number)+1
        fp.seek(0,0)
        fp.write(str(new_number))
        print("number stored")
        return number

if __name__=="__main__":
    getUniqnum()