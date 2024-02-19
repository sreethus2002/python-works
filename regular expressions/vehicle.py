#vehicle kl-09-AD-1245

from re import*
txt=input("enter a vehicle number")
Pattern="(KL)[-\S][\d]{2}[-\s][A-Z]{1,2}[-\s][\d]{4}"
matcher=fullmatch(Pattern,txt)
if matcher==None:
    print("invalid")
else:
    print("valid")