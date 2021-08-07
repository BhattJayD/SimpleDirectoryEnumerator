
import requests
import sys
subList=open('wordlist2.txt').read()

DirList=subList.splitlines()

for dir in DirList:
    dirEnum=f"http://{sys.argv[1]}/{dir}.html"
    r=requests.get(dirEnum)
    if r.status_code==404:
        pass
    else:
        print("Dir is:",dirEnum)




