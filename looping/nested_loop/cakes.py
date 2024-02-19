cakes=[
    {"id":1,"name":"blueberry","shape":"circle","varients":[
        {"weight":"0.5kg","price":400},
        {"weight":"1kg","price":800}
    ]},
     {"id":2,"name":"vancho","shape":"square","varients":[
        {"weight":"0.5kg","price":500},
        {"weight":"1kg","price":1000}
    ]},
    {"id":1,"name":"chocalate","shape":"heart","varients":[
        {"weight":"0.5kg","price":600},
        {"weight":"1kg","price":1200}
    ]},
      {"id":1,"name":"cheese","shape":"rectangle","varients":[
        {"weight":"0.5kg","price":650},
        {"weight":"1kg","price":1300}
    ]},
    
]

#below 500
for cak in cakes:
    for v in cak.get("varients"):
        if v.get("price")<=500:
            print(cak.get("name"))

price_filter=[cak.get("names")for cak in cakes for v in cak.get("varients") if v.get("price")<=500]
print(price_filter)


#round shape 

sp=[cak.get("name")for cak in cakes if cak.get("shape")==("square")]
print(sp)


#cake names
name_filter=[cak.get("name")for cak in cakes]
print(name_filter)

#1kg and round

shape_filter=[cak.get("name")for cak in cakes for v in cak.get("varients") if v.get("weight")==("1kg") and cak.get("shape")==("circle")]
print(shape_filter)

#print 0.5 kg,cheese

wn=[v.get("price")for cak in cakes for v in cak.get("varients") if v.get("weight")==("0.5kg") and cak.get("name")==("cheese")]
print(wn)

#1kg names
name=[cak.get("name")for cak in cakes for v in cak.get("varients") if v.get("weight")==("1kg") ]
print(name)