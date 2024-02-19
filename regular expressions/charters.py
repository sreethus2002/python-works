from re import *
text="abaabcaabaaaa"
#pattern="[abc]" #full lowercase check pattern="[a-z]"

#pattern="[A-Z]"

#pattern="[0-9]"

#pattern="[a-zA-Z0-9]"

#pattern="[^a-z]" exclude lower case alphabet

#pattern="[^a-zA-Z]" exclude all alphabet

#pattern="[^a-zA-Z0-9]"

#pattern="\d" #[0-9] meaning predefined digit representation

#pattern="\D" #[^0-9] meaning exclude digit representation

#pattern="\w" #[a-zA-Z0-9] meaning alphanumeric charcters representation

#pattern="\W" #[^a-zA-Z0-9] meaning exclude alphanumeric charchter representation

#pattern="a+" #+ atleast one a

#pattern="a*" # matches any number of a

#pattern="a?" # optional

#pattern="a{2,3}" # minimum 2 and maximum 3

#pattern="a{2}"# minimum 2 a

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
