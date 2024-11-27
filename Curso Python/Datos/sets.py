#set{}: Coleccion desordenada de elementos unicos mutable
# Se pueden añadir y eliminar pero no cambiar 

conjunto = {1,1,2,2,3}

conjuntoC = set(("Esto","no","esta","ordenado"))

print(conjuntoC)

if"ordenado" in conjuntoC:
    print("Esta")

telefono = {"Xiaomi","Patata"}
telefono2 = ["Nokia","Xiaomi"] #puede ser cualquier coleccion 

telefono.add("Patata")
telefono.update(telefono2)

#Elimina

meta = {"Predaplanta","Shiranui","Zombie","Cubicos"}
meta2 = {"Matemeka","CronoMalo","Escritoribot"}
meta.remove("Cubicos")
meta.discard("Zombie")
meta.pop() # Borra random
meta.clear #Borra todo

#recorrer

for juego in meta2:
    print(juego)


tuplaO =[]
for juego in meta2:
    if "o" in juego:
        tuplaO.append(juego)

print(tuplaO)

a = {1,2,3,4,5}
b = {1,3,5,7,9}

c = a.union(b)

i = a.intersection(b)

d = a.difference(b)

ds = a.symmetric_difference(b)
