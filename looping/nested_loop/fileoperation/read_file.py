#f=open("file path","node")

f=open("C:\\Users\\sreet\\OneDrive\\Desktop\\july_pythonworks\\looping\\nested_loop\\fileoperation\\data.txt","r")

words=[line.rstrip("\n") for line in f]
print(words)