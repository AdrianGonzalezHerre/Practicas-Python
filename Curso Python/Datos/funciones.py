def funcion(dios, pasa):
    print(f"El {dios} utiliza unicamente {pasa}")

funcion("Zeus","la pinga")

def nombreGenericonumero84(Lunes,left,me,broken):
    meme = left
    print(f"El {Lunes}", meme + f" {me} totalmente {broken}")

nombreGenericonumero84("Dia","meme","se fue",0)

def llamarMultiple(*multiple):
    print(f"Este es el numero {multiple[0]}")
    print(f"Luego de ese viene el {multiple[1]}")

llamarMultiple(1,2,3)

def muymultiple(**numeros):
    print(f"El pokemon tcg es {numeros["adjetivo"]}, y yo uso {numeros["mazo"]}")

muymultiple(adjetivo = "Malo", mazo = "Pika")


#VAriables por defecto 
def decirMalo(malo = "Adrian"):
    print("Quien es malo ? \n"+ malo)

decirMalo("Yo")
decirMalo()

#Return

def suma(a,b):
    return a+b
    
def resta(a,b):
    return a-b

print(suma(10,2))

#Recursividad

def factorial(n):
    if n == 0:
        return 0
    else:
        return n*factorial(n-1)