vocal=("a","e","i","o","u")
consonante=("b","c","d","f","g","h","j","k","l","m","n","p","q","p","r","s","t","v","w","x","y","z")
letra=input("ingrese letra:")
if letra in vocal:
    print(letra,"es una vocal")
else:
    print(letra,"es una consonante")