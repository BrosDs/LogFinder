__author__ = 'DarioStabili'

import shutil
import glob
import os
import hashlib

def checkLogs():
    for root, dirs, files in os.walk("received/"):
        path = os.path.join(root,'*.txt')
        for f in glob.glob(path):
            with open(f, "r") as content_file:
                content = content_file.read()
                vals = content.split("#DIGESTEND#")
                rDig = vals[0]
                body = vals[1]
                cDig = hashlib.sha512(body.encode("utf-8")).hexdigest()
                if rDig == cDig:
                    print(f+": not corrupted")
                    moveLog(f,1)
                else:
                    print(f+": corrupted\nreceived: "+rDig+"\ncalculated: "+cDig)
                    moveLog(f,2)
    flushAll()


def moveLog(logname, dest):
    if dest == 1:
        new = logname.replace("received","ok")
        shutil.copy2(logname, new)
    elif dest == 2:
        new = logname.replace("received","corrupted")
        shutil.copy2(logname, new)

def flushAll():
    dirPath = "received"
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        os.remove(dirPath+"/"+fileName)