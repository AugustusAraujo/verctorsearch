import os
import json

files = os.listdir("./db")
    
entries = []

def gen_entry(file):
    tokens = file.read().replace(",", "").replace("?","").replace(".","").split(" ")
    items = dict()

    for t in tokens:
        name = t.lower()
        item = items.get(name)
        if item is None:
            items.update({f"{name}": 1})
        else:
            items.update({f"{name}": item+1})
            
    entries.append(dict(
        items=items,
        meta=file.name
    ))

for f in files:
    filename = os.path.join("./db", f)
    if os.path.isfile(filename):
        item = open(filename, "r")
        gen_entry(item)

indexes = []

def add_term(term):
    if term not in indexes:
        indexes.append(term)        

for i in entries:
    for j in i["items"].keys():
        add_term(j)

indexes.sort()

def plot():
    final = []
    for i in entries:
        d = dict()
        for j in i["items"].keys():
            index = indexes.index(j.lower())
            # count de cada item com a key sendo o index do value
            d.update({str(index): i["items"].get(j)})
        d.update({"meta": i["meta"]})
        final.append(d)
    
    return final


# SEARCH
inp = input("Search: ")
# pegar a string e ver se tem o termo no index. se tiver o termo add numa array pra buscar em um or se tem algum dos itens da array em um plot, aí depois retorna o plot

