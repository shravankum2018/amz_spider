import json
path = r"C:\Users\SSD\Dropbox\SCRAPY\PROJECTS\newProjects\amazon\amazon\charger2.json"
file = open(path)
data=json.load(file)
for d in data:
    r = d["reviews"]
    p =d['price']
    rat = d['ratigs']
    u=d['id']
    n=d['name']
    
    if (rat>=4.2):
        print(f"Price: {p}  reviews: {r}  ratings: {rat} title: {n} id : https://www.amazon.in/gp/product/{u}")