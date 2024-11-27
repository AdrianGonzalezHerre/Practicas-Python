import pandas as pd


def cm_a_pulgada (cm):
    return cm/2.54

df = pd.read_excel("medidas.xlsx")

df["Pulgada"] = df["Centimetros"].apply(cm_a_pulgada)

df.to_excel("medidas_convertidas.xlsx",index=False)

print("Conversión completada y guardada en un nuevo archivo llamado 'medidas.xlsx'")