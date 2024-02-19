# initializing instance variables

class book:
    author:str
    name:str
    publisher:str
    def __init__(self,author,name,publisher):
        self.author=author
        self.name=name
        self.publisher=publisher
    def display(self):
        print(self.author,self.name,self.publisher)
    def __str__(self):
        return self.name
    
obj1=book("twlight","emya","dc")
obj1.display()



