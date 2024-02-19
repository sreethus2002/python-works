def swap_nums(fn):
    def inner_functions(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner_functions
@swap_nums
def sub(n1,n2):
    return n1-n2
@swap_nums
def div(n1,n2):
    return n1/n2
print(sub(2,10))
print(div(2,8))


