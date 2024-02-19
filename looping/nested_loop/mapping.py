lst=[3,6,1,2,8]

#[] if num<5 num-1 num>5 mum+1

map_num=[num+1 if num>5 else num-1 for num in lst]
print(map_num)