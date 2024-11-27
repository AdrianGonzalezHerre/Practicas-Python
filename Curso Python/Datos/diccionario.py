
#dict (dictionary){}: Coleccion de pares clave-valor desordenada y mutable ArrayList ?

diccionario ={
    "nombre": "Yo",
    "edad": 11,
    "amigos":["Edgard", "Yera"],
    "gustos":{"souls":"bloodborne","pito":True},
}

conDicc = dict(nombre = "Yo", descripcion = "Malo")

amigo= diccionario["amigos"]
des = conDicc.get("descripcion")
value = diccionario.values()
items = diccionario.items()

#print(amigo)

#Cambio valor

diccionario ["amigos"] = ["Edgard", "Manu"]

#Agregar

diccionario["rangos"] = ['Leyenda','Kog']

#print(diccionario)

#Eliminar

diccionario.pop("amigos")
diccionario.popitem()
#diccionario.clear()

#Recorrer

for key in diccionario:
    print(f"{key} : {diccionario.get(key)}")

for x in diccionario.values:
    print(x)




