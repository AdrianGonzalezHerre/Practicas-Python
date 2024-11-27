# Bucle For

lenguajes = ["Python", "Java", "C"]
x = 1

for tecnologia in lenguajes:
    if tecnologia=="C":
        break
   #print(f"{x}. {tecnologia}")
    x+=1


y = 0
txt = "Puedo recorrer el texto con el for"

for caracter in txt:
    print(caracter)
    #y+=1
    #print(txt[y-1]) Hacen lo mismo 


for x in range(8):
    print(x)
else:
    print("Pablito no sabe contar mas")

impares=[1,3,5]
pares = [2,4,6]

for i in impares:
    for p in pares:
        print(i,p)