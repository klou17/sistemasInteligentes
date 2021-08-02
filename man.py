import pandas as pd

#Creamos el Dataframe, con tres ordenadores
#_________________________________________________________________________
ordenadores_df = pd.DataFrame({'RAM':[16, 8, 12],
                               'Nucleos_procesador':[8, 4, 8],
                               'Horas_autonomiaa':[8, 12, 7]})

#Creamos nuestra formula manhattan y la aplicamos a los tres ordenadores
#_________________________________________________________________________
def distancia_manhattan(a, b):
    return sum(abs(a - b))
  
print(distancia_manhattan(ordenadores_df.iloc[0], ordenadores_df.iloc[1])) # Distancia de 16
print(distancia_manhattan(ordenadores_df.iloc[0], ordenadores_df.iloc[2])) # Distancia de 5
print(distancia_manhattan(ordenadores_df.iloc[1], ordenadores_df.iloc[2])) # Distancia de 13
