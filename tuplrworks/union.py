st1={"red","green","blue","purple"}
st2={"red","purple","green","blue"}

diff_set=st1.difference(st2)
print(diff_set)


union_set=st1.union (st2)
print(union_set)


#intersection
intersection_set=st1.intersection(st2)
print(intersection_set)

#remove


st1.remove("red")
print(st1)

#discard -there is is no element in the set ,it returns that set
#eg- st1=("red","blue")
#st1.discard("white")
#ans -("red","blue")


st1.discard("white")

#subset

print(st1.issubset(st2))

#superset



print(st1.issuperset(st2))


