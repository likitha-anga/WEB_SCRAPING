import json 
from bs4 import BeautifulSoup
with open ("imdb 1_task.json","r") as f:
    a=json.load(f)
    # print(a)
i=0
b=[]
dic={}
while i<len(a):
    l=a[i]["url"]
    # print(l)
    k=l[-10:-1]
    b.append([k])
    dic['id']=b
    # print(k)
    i=i+1
    # print(dic)
with open("imdb 8_task.json","w")as file:
    json.dump(dic,file, indent=2)
    
  
  