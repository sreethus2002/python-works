# usa moblie number
from re import*
text=input("enter a mobile number")
pattern="[0-9]{3}[-\s]?[0-9]{3}[-\s]?[0-9]{4}"
matcher=fullmatch(pattern,text)
if matcher==None:
    print("invalid")
else:
    print("valid")