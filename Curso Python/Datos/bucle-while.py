#Bucle While

x = 1

while x<=10:
    print("x vale", x)
    if x == 5:
        #continue Repite el bucle desde el punto que lo pones 
        break
    x +=1
else:
    print("Se termino el bucle")


# Input

while True:
    respuesta = input("Desea seguir? (s/n)")
    if respuesta.lower() == "s":
        print("Okey")
        break
    else:
        print("Se sigue")