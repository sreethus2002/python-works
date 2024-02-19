# pancard number

from re import*
txt=input("enter pancard number")
pattern="[A-Z]{3}[PCAFHT]+[A-Z]{1}\d{4}[A-Z]{1}"
matcher=fullmatch(pattern,txt)
if matcher==None:
    print("invalid")
else:
    print("valid")