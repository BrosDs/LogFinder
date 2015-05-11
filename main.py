__author__ = 'DarioStabili'

import glob
import os
import platform
import hashlib
import server

def findLog():
    root = ""
    if platform.system() == "Windows":
        print("Windows")
        root = "C:/"
    else:
        print("Not Windows")
        root = "/"

    out_file = open("log_list.txt","w")
    for root, dirs, files in os.walk(root, topdown=True):
        path = os.path.join(root,'*.log')
        for f in glob.glob(path):
            print(f)
            out_file.write(f+"\n")
    out_file.close()

def signLogs():
    log_list = open("log_list.txt","r")
    index = 0
    while True:
        index=index+1
        logpath = log_list.readline()

        if logpath == "":
            break
        #print(logpath)
        with open(logpath.rstrip('\n'), "r") as content_file:
            content = content_file.read().encode('utf-8')
            dig = hashlib.sha512(content).hexdigest()
            signedLog = open(str(index)+".txt","w")
            signedLog.write(dig+"#DIGESTEND#"+content.decode('utf-8'))
            signedLog.close()
    log_list.close()



if __name__ == "__main__":
    #findLog()
    signLogs()
    server.checkLogs()
