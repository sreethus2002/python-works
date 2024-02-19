class parent:
    def mobile(self):
        print("vivo")

    def car(self):
        print("thar")
class child(parent):
    def mobile(self):
        print("iphone")
ch=child()
ch.mobile()
ch.car()
