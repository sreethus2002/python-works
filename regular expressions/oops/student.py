#student rolnum,course,total

class student:
    rol:int
    course:str
    total:int

    def __init__(self,rolnum,course,total):
        self.rol=rolnum
        self.course=course
        self.total=total
    def display(self):
        print(self.rol,self.course,self.total)

obj1=student(1000,"django",450)
obj1.display()
