class parent:
    def vehicles(self):
        self.context=["passinpro","swift"]
        return self.context
class child(parent):
    def vehicles(self):
        self.context=super().vehicles()
        self.context.append("ola")
        return self.context
p=parent()
print(p.vehicles())
c=child()
print(c.vehicles())