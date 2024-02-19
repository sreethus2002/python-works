class p1:
    def m1(self):
        print("inside parent1")

class p2(p1):
    def m2(self):
        print("inside parent2")

class child(p2):
    def m3(self):
        print("inside parent")

ch=child()
ch.m1()