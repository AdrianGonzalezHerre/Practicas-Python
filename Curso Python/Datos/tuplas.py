#Tuplas

#tuple() Array no modificable

souls = ("Dark Souls","Blodborne","Elden Ring")

largo = len(souls)
tipo = type(souls)
constructor = tuple(("El Dark souls",2, "es mejor"))

best = souls[1]
#Lo mismo con rangos que list 

#Castear

listaFromSoft = list(souls)
listaFromSoft.append("Sekiro")
listaFromSoft[1] = "PC " + listaFromSoft[1]
souls = tuple(listaFromSoft)
print(souls)

#Desempaquetar

(a,b,c,d) = souls

(soul1, blod, *newGen) = souls

print(newGen)


#Recorrer

for juego in souls:
    print(juego)

for i in range(len(souls)):
    print(i+1,souls[i])

tuplaO =[]
for juego in souls:
    if "o" in juego:
        tuplaO.append(juego)

print(tuplaO)

#Join 

soulLike = ("Code Vein", "NiOH")

todo = souls + soulLike
