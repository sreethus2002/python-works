num1=10
num2=200
num3=30
if((num1>num2 and num1>num3)):
    if(num2>num3): 
        print(f"{num2} second largest muber")
    else:
        print(f"{num3} second largest number")
elif(num2>num3 and num2>num1):
    if(num1>num3):
     print(f"{num1} second largest number")
    else:
       print(f"{num3} second largest number")
elif(num3>num1 and num3>num2):
    if(num2>num1):
      print(f"{num2} second largest number")
    else:
      print(f"{num1} second largest number")        
    
