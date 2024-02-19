# validate python variable name

from re import*
varname=input("enter a variable name")
Pattern="[a-zA-Z][a-zA-Z0-9_]*"
matcher=fullmatch(Pattern,varname)
if matcher==None:
    print("invalid")
else:
    print("valid")
