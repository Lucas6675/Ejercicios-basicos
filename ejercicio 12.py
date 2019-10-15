N=int(input("Ingrese un valor: "))
factorial=1
suma=0
for i in range(1,N+1):
    factorial=1
    for j in range(1,i+1):
        factorial*=j
    suma+=factorial
        
print(suma)