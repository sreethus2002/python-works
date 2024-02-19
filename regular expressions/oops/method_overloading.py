#function overloading

#same function name or method name but different number of parameters
class operations:
    def add(self,n1,n2):
        return n1+n2
    def add (self,n1,n2,n3):
        return n1+n2+n3
    def add (self,n1,n2,n3,n4):
        return n1+n2+n3+n4
    
op=operations()
print(op.add (10,20,30,40))