from abc import ABC,abstractclassmethod
class editor(ABC):
    @abstractclassmethod
    def debug(self):
        pass
    def run(self):
        pass
    def save(self):
        pass
class vscode(editor):
    def debug(self):
        print("vscode debug")
    def run(self):
        print("vscode run")
    def save(self):
        print("vscode save")

obj=vscode()
obj.debug()

