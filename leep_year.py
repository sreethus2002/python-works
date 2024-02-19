year=2100
if(year%100==0 and year%400==0):
    print(f"{year} is a leep year")
elif(year%100!=0 and year%4==0):
    print(f"{year} is a leep year")  
else:
    print(f"{year} is not a leep year") 
