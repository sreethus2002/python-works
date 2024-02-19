
class mobiles:
    data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
        

    ]
#create

    def create(self,*args,**kwargs):
         self.data.append(kwargs)
         return f"{kwargs}created !!"
    
    def retrieve(self,id,*args,**kwargs):
         obj=[mob for mob in self.data if mob.get("id")==id].pop()
         return obj
    def get(self,*args,**kwargs):
         return f"{self.data}"
    def put(self,id,*args,**kwargs):
         obj=[mob for mob in self.data if mob.get("id")==id].pop()
         return f"{obj} updated"
    def destroy(self,oid,*args,**kwargs):
         obj=[mob for mob in self.data if mob.get("id")==id].pop()
         self.data.remove(obj)
         return f"{obj} has been removed"
         
    

obj=mobiles()
#print(obj.create(id=105,name="realme",price=10000))
#print(obj.retrieve(id=103))
#print(obj.get())
#print(obj.put(id=104,name="nokia"))
print(obj.destroy(id=101))