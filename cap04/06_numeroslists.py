for value in range(0,5):
    print(value)
for valor in range(10):
    print(valor)
numeros=list(range(5,10,2)) #el tercer argumento es opcional, indica el paso
print(numeros)

cuadrados=[]
for valores in range(1,11):
    cuadrado=valores**2
    cuadrados.append(cuadrado)
    #cuadrados.append(valores**2)
print(cuadrados)

cuads=[valora**2 for valora in range(1,11)]
print(cuads)

digitos=[1,2,3,4,5,6,7,8,9,0]
print(digitos)
print("mínimo: ",min(digitos))
print("máximo: ",max(digitos))
print("suma:",sum(digitos))