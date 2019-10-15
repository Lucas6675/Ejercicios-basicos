N=int(input("Ingrese un valor: "))
resto=0
binario=0
texto=""
for i in range(0,4):
    resto = N%2
    N=int(N/2)
    texto+=str(resto)
print(texto)