"""Variables
    Es un contenedor para almacenar datos
    Va a tener nombre
    Es creado la primera vez que se asigna el valor    
"""

x = 5
X = "Distinto a x"
txt ="Texto"

print(x)
print(X)
print(txt)


x,y=8,2

print(str(x) + " y " + str(y))

frutas = ["platano","nectarina","paraguayo"]
a,b,c = frutas

newtxt = "Curso"
newtxt2 = "de"
newtxt3 = "Python"

print(newtxt, newtxt2, newtxt3) # Se puede con + y concatena con las , crea un espacio

num1 = 1
num2 = 2

print(newtxt,num2)

variableext = "se puede"

def funcion():
    global variableInterna #No lo voy a usar en la vida
    variableInterna = "No se puede"
    variableext = "Si lo cambio aqui no se ve fuera"
    print(variableInterna)
    print(variableext)
funcion()
print(variableext)