#Listas

array = [1,2,3,4,5]
arrayS = ["meme", "lol", "kneeSurgey"]
arrayMixta = ["Numeros",5,True]
constructor = list(("Dragon",57,None))

parte = array[1:4]
inicio = array[:3]
final = array [2:]

if "lol" in arrayS:
    print("Esta")
else:
    print("No esta")


modificar= ["Mario","Link","DK","Pika","Ness"]

#Añadir
modificar[2] = "Samus"
modificar.insert(3,"Captain Falcon")
modificar.append("Fox")

dlc = ["Joker", "Banjo", "Hero"]
dlc.clear()
modificar.extend(dlc)

# Quitar

modificar.remove("Fox")
modificar.pop()
modificar.pop(0)
del modificar[2]
dlc.clear() #Elimina

print(modificar)

#Recorrer

for personaje in modificar:
    print(personaje)

for i in range(len(modificar)):
    print(i+1,modificar[i])

listaI =[]
for pj in modificar:
    if "i" in pj:
        listaI.append(pj)

print(listaI)

#Ordenar

modificar.sort() #alfabetico u ordenado mayor menor 
modificar.sort(reverse=True)

#Copiar 

brawl = ["Ike", "Toon link", "Lucas"]
wiiU =["Megaman", "Daraen", "Pac-man"]

union = brawl+wiiU
brawl.extend(wiiU)
