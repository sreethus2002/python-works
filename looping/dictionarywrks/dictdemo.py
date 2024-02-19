#dict_name={"key":"value","key":"value"}

student={"name":"sreethu","age":21,"college":"vkcet"}
print(student["name"])

if "age" in student:
   print("present")
else:
    print("not present")      

student["course"]="django"
print(student)

#if updation

student["course"]+="python"
print(student)

mobile={"name":"realme","ram":8,"clr":"black"}
print(mobile["name"])
if "ram" in mobile:
    print("present")
else:
    print("not present")

mobile["price"]=100000

mobile["offer"]=1000
mobile["price"]-=1000
print(mobile)