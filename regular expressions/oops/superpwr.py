class superpowers:
    def __init__(self,name):
        self.name=name
    def super_powers(self):
        self.context=["run","jumb"]
class spiderman(superpowers):
    def super_powers(self):
        self.context=super().super_powers()
        self.context.append("fly")
        self.context.append("spiderweb")
        return self.context

class minnalmurali(superheros):
    def super_powers(self):
        self.context=super().super_powers()
        self.context