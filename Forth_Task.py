import requests
import json 
from bs4 import BeautifulSoup
with open("imdb 1_task.json","r") as file:
    mov=json.load(file)
    i=0
    url=[]
    while i<len(mov):
        print(i+1,":",mov[i]["name"])
        url.append(mov[i]["url"])
        i=i+1
    mov_num=int(input("enter the number:"))-1
    b=url[mov_num]
    c=requests.get(b)
    soup=BeautifulSoup(c.content,"html.parser")
    con=soup.find('script',type='application/ld+json').text
    a=json.loads(con)
    dic={}
    # print(a)
    for i in a:
        dic['name']=a['name']
        dic['director']=[a['director'][0]['name']]
        dic['image']=a['image']
        dic['description']=a['description']
        dic["language"]=a['review']['inLanguage']
        dic['genre']=a['genre']
        dic['country']='india'
    # print(dic)
with open("imdb 4_task.json","w") as file:
    json.dump(dic,file,indent=8)