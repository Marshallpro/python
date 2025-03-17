print("enter any string to encript")
name=input()

for x in range(len(name)):
     name=name.replace("k"or"K","A")
     name=name.replace("j"or"J","I")
     name=name.replace("P"or"p","O")
     name=name.replace("t"or"T","E")
     name=name.replace("f"or"F","U")
     
print(name)   
