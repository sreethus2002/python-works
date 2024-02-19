
from re import* 
text="ababcdABabac"

pattern="ab"
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start())
    print(m.group())
    count=count+1
print("occurance of pattern=",count)