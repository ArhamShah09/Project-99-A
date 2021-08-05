import time
import os
import shutil

path = input("Enter the path of the file : ")
days = 30
seconds = time.time()-(days*24*60*60)

if(os.path.exists(path)):
    for root,dirs,files in os.walk(path):
        if(seconds > os.stat(path).st_ctime):
            shutil.rmtree(path)