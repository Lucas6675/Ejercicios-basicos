n=int(input("Ingrese vlaor: "))
m=int(input("Ingrese otro valor: "))
o=int(input("Ingrese un tercer valor: "))

if (n>m) and (n>o):
    if (m>o):
        print(n,m,o)
    else:
        print(n,o,m)
if (m>n) and (m>o):
    if (n>o):
        print(m,n,o)
    else:
        print(m,o,n)
if (o>m) and (o>n):
    if (m>n):
        print(o,m,n)
    else:
        print(o,n,m)