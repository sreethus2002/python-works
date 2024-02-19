lst=[i for i in range(1,8)]
days=["holiday" if  i in (1,7) else "weekday" for i in lst]
print(days)

#print all +ve numbers that are divisible by 3

lst=[2,3,4,6,-1,0,5,8]
nums=[ num for num in lst if num>0 and num%3==0]
print(nums)

num=int(input("enter a number"))
prime=[num %i==0 for i in (2,num)]
print(prime)