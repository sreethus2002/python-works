num=int(input("enter a number"))
is_prime=True
for i in range(2,num):
    if(num%2==0):
        is_prime=False
if(is_prime==True):
    print("prime number")
else:
    print("not prime")