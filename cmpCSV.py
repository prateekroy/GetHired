
import io
import os
from os.path import isfile, join
import re
# import pandas as pd
class Recruiter:
    def __init__(self,line=""):
        spl=line.split(',')
        self.firstname=spl[0]
        self.lastname=spl[1]
        self.emailid=spl[2]
        self.org=spl[3]
        self.position=spl[4]

class Contacts:
    def __init__(self):
        self.cstack=[]

    def readfiles(self):
        dirPath = '.\\'
        fileNameList = [filename for filename in os.listdir(dirPath) if isfile(join(dirPath,filename)) and ".csv" in filename ]
        # print(fileNameList)
        for filename in fileNameList:
            with io.open(filename, 'rU', encoding='utf-8') as clist:
                lc=1
                for line in clist:
                    if lc:
                        lc-=1
                        continue
                    contact = re.findall(r'^(.*),"\d.*',line)[-1]
                    if not contact in self.cstack:
                        rec=Recruiter(contact)
                        self.cstack.append(rec)
                    # print(contact)
        return self.cstack

