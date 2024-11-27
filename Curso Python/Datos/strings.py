# str String

texto = "   Este es un texto                "

comillassimple = 'Texto'
comillasdoble = "Texto"
comillastriple ="""Texto
                    con espacio"""
comillassimpletriple = '''Texto con
                            espacio'''

#Array de caracteres

caracter = texto[1]
print(caracter)

#Len length

longitud = len(texto)
print(longitud)

# In Lo incluye
print("texto" in texto)
print("pito" not in texto)

# Slice fragmentar 

print(texto[5:10])

#Upper Lower Strip Split Replace

mayus = texto.upper()
minus = texto.lower()
noEspacios = texto.strip()

print(mayus)
print(minus)
print(noEspacios)

remplazo= texto.replace("texto", "lol")

textoComas = "Asi, es, como, escribo, de, verdad"
separar = textoComas.split(",")
print(separar)


#Metodos usados

desordenado= "NO SE ESCRIBIR"
capital =desordenado.capitalize() #Primer en mayuscula

inicio= desordenado.startswith("NO")
final = desordenado.endswith("ESCRIBIR")

titulo= desordenado.title() #Cada espacio con mayus

contador = desordenado.count("E")
encontrar = desordenado.find("SE")


#Concatenar 

a = "uno"
b = "dos"
c = a + " " +b

#F-String Texto con variables 

num = 13
nombre ="Peter"

txt=f"La edad de {nombre} es {num}"
print(txt)

# Escapes 

escape = "Quiero escapar de \"Venezuela\" por dios"
saltolinea = "Arriba \n Abajo"