
import pandas as pd 

data = {
    "Pieza" : ["Pata","Tablero","Puerta","Estante","Panel"],
    "Centímetros" :[40,120,60,30,180]
}

df = pd.DataFrame(data)

df.to_excel("medidas.xlsx",index=False)

print("Conversión completada y guardada en un nuevo archivo llamado 'medidas.xlsx'")