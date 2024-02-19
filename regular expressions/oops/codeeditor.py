class editor:
    name:str
    def __init__(self,name):
        self.name=name

    def spec(self):
        pass
class vscode(editor):
    def spec(self):
        print(f"{self.name} support edit,debug,run,extension support")

    def __str__(self):
        return self.name
    
vobj=vscode("vscode")
vobj.spec()
print(vobj)
    
