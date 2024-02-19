num1=int(input(" enter value for num1"))
num2=int(input("enter value for num2"))
larg_num=num1 if num1>num2 else num2

#with equation
small_num=num1 if num1<num2 else num2
for i in range(1,small_num+1):
    if num1%i==0 and num2%i==0:
       gcd=1
lcm=(num1*num2)/gcd
print(lcm)

#without equation
num1=int(input("enter value for num1"))
num2=int(input("enter value for num2"))
product=num1*num2
for i in range(large_num,product+1):
    prtint(i)
    if i%num1==0 and i%num2==0:
        lcm=i
        break
print(lcm)