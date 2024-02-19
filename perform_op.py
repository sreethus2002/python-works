def perform _operation(*args,**kwargs):
num1,num2=args
op=kwargs.get("operand")
if op=="+":
    return num1+num2
elif op=="-":
    return num1-num2
elif op=="*":
    return num1*num2
else:
    return "invalid operand"

print(perform_operation(10,20,operand="n"))