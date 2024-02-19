# rule for validating mobile number


from re import*
mob=input("enter mobile number")
pattern="(91)?[0-9]{10}"
matcher=fullmatch(pattern,mob)
if matcher==None:
    print('inavlid')
else:
    print("valid")
