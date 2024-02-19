words="pneumonoultramicroopicslicovolcanoconiosis"
vowels='a','e','i','o','u'
v_count=0
c_count=0
for ch in words:
    if ch in vowels:
        v_count+=1
    elif ch.isalpha():
        c_count+=1
print(v_count)
print(v_count)
