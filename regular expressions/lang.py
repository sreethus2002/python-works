#starting with an alphbet k,l,m,n
# second that must be adigit an divisible by 3
# followed by any number of alphabets and digits


from re import*
varname=input("enter a text")
pattern="[k-n][369][a-zA-Z0-9]*"
matcher=fullmatch(pattern,varname)
if matcher==None:
    print("invalid")
else:
    print("valid")