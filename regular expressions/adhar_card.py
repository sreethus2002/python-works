#rule for validation adhar number (with or without space)

from re import*
txt=input("enter a adhar number")
pattern="[\d]{4}(\s)?[\d]{4}(\s)?[\d]{4}"
matcher=fullmatch(pattern,txt)
if matcher==None:
    print("invalid")
else:
    print("valid")