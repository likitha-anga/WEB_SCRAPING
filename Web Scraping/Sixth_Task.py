import json
import requests
with open ('imdb 5_task.json','r') as file:
    c=json.load(file)
empty_dict={}
i=0
eng_slang=0
mal_slang=0
hin_slang=0
while  i<len(c):
    if c[i]['language']=='English':
        eng_slang=eng_slang+1
        empty_dict['English']=eng_slang
    if c[i]['language']=='Malyalam':
        mal_slang=mal_slang+1
        empty_dict['Malyalam']=mal_slang
    else:
        empty_dict['Malyalam']=mal_slang
    if c[i]['language']=="hindi":
        hin_slang=hin_slang+1
        empty_dict['hindi']=hin_slang
    else:
        empty_dict['hindi']=hin_slang 
    i=i+1
with open ("imdb 6_task.json","w") as file:
    json.dump(empty_dict,file,indent=4 )
    