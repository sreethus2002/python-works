
data=[
    {"id":100,"name":"python","price":350},
    {"id":101,"name":"java","price":450},
    {"id":102,"name":"django","price":1300},
    {"id":103,"name":"html","price":1000},
    {"id":104,"name":"bootstrap","price":300}
]

#(a)list all books

all_book_names=[da.get("name") for da in data]
print(all_book_names)

def retrieve(*args,**kwargs):
    id=kwargs.get("id")
    obj=[m for m in data if m.get("id")==id].pop()
    return obj

print(list())
print(retrieve(id=100))



