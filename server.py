__author__ = 'BrosDs'

import glob
import os
import hashlib

def checkLogs():
    for root, dirs, files in os.walk("received/"):
        path = os.path.join(root,'*.txt')
        for f in glob.glob(path):
            with open(f, "r") as content_file:
                content = content_file.read()
                vals = content.split('#')
                rDig = vals[0]
                body = vals[1]
                cDig = hashlib.sha512(body.encode("utf-8")).hexdigest()
                if rDig == cDig:
                    print(f+": not corrupted")
                else:
                    print(f+": corrupted\nreceived: "+rDig+"\ncalculated: "+cDig)
