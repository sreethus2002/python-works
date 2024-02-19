all_users=["mammotty","mohanlal","prithvi","asif","dq","fahad","nivin"]
nivin_friends=["asif","dq","fahad"]

#nivin_suggestions

st1=set(all_users)
st2=set(nivin_friends)

st1.discard("nivin")

diff_set=st1.difference(st2)
print(diff_set)


dq_friends=("mammotty","asif","fahad","mohanlal")

st3=set(dq_friends)
mutual_frnds=st2.intersection(st3)
print(mutual_frnds)        