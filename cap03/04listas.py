objetos = ["mouse","celular","computador","pantalla"]
print(objetos)
print(objetos[1])
print(objetos[3].title())
objetos.append("tazón")
print(objetos)
objetos.insert(0,"calendario")
print(objetos)
del objetos[1]
print(objetos)
objetos.pop(2)
print(objetos)
objetos.remove("pantalla")
print(objetos)
objetos.sort(reverse=True) #objetos.sort()
print(objetos)
#objetos.reverse()
print(len(objetos))