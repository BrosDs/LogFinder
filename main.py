__author__ = 'DarioStabili'

import glob
import os
import platform

def main():
    root = ""
    if platform.system() == "Windows":
        print("Windows")
        root = "C:/"
    else:
        print("Not Windows")
        root = "/"

    for root, dirs, files in os.walk(root, topdown=True):
        out_file = open("log_list.txt","w")
        path = os.path.join(root,'*.log')
        for f in glob.glob(path):
            print(f)
            out_file.write("f")
        out_file.close()

if __name__ == "__main__":
    main()