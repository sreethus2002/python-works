for num in range(1800,2025):
    if(num%100==0 and num%400==0):
       print(num)
    elif(num%100!=0 and num%4==0):
        print(num)

    