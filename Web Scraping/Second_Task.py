import json
with open("imdb 1_task.json","r") as file:
    movies=json.load(file)
def movie_by_year():
    dict={}
    for i in movies:
        list=[]
        year=i["year"]
        if year not in dict:
            for j in movies:
                if year==j["year"]:
                    list.append(j)
            dict[year]=list
        # print(dict)
    with open("imdb 2_task.json","w")as file:
        json.dump(dict,file, indent=8, sort_keys=True) 
movie_by_year()
