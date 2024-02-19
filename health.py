gender="female"
tummy_size=34
buttock_size=75
value=tummy_size/buttock_size
print(value)
if(value<=0.80):
    print("low")
elif(value>=0.81 and value<=0.85):
    print("moderate")
elif(value>=0.86):
    print("high")
elif(gender==male):
    if(value<=0.95):
        print("low")
    if(value>=0.96 and value<=1.0):
        print("moderate")
    else:
         print("high")
          
