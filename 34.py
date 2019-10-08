n=int(input("Ingrese valor: "))
m=int(input("Ingrese otro valor: "))
o=int(input("Ingrese un tercer valor: "))

if (n<m) and (n<o):
    if (m<o):
        print(n,m,o)
    else:
        print(n,o,m)
if (m<n) and (m<o):
    if (n>o):
        print(m,o,n)
    else:
        print(m,n,o)
if (o<m) and (o<n):
    if (m<n):
        print(o,n,m)
    else:
        print(o,m,n)