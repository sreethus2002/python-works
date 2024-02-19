#inheritance
#polymorphism
#abstraction
#encapulasation


class parent:
    def mobile(self):
        print("iphone")

    def bike(self):
        print("interseptor 650")
class child(parent):
    pass

obj=child()
obj.mobile()
obj.bike()
