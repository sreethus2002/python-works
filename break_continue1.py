lst=[10,11,12,13]
num=3
for i in range(0,len(lst)):
    if num==lst[i]:
        print("element not found")
        break
else:
    print("element not found")