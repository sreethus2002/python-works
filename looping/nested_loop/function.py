def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2
def cube(n):
    return n**3
def product(n1,n2):
    return n1*n2
def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1
print(smart_sub(6,9))
def fact(n):
    