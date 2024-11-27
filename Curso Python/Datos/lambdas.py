
#Funciones de una sola linea de codigo

def suma(a,b):
    return a+b
    
def resta(a,b):
    return a-b

#ejemplo sos
suma_lambda= lambda a,b :a+b
resta_lambda= lambda a,b :a-b
print(suma(10,2))

#ejemplo god
def multiplica(n):
    return lambda a: a*n

duplicaador = multiplica(2)

#filter

numeros = [1,2,3,4,5,6,7,8,9]

pares = list(filter(lambda x: x % 2 ==0 , numeros))