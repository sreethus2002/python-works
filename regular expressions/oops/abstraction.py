from abc import ABC,abstractclassmethod
class car(ABC):
    @ abstractclassmethod
    def start(self):
        pass
    def accelerate(self):
        pass
    def stop(self):
        pass
class swift(car):
    def start(self):
        print("swift start method")
    def accelerate(self):
        print("swift accelerate method")
    def stop(self):
        print("swift stop method")

obj=swift()
obj.start()