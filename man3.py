import pandas as pd

ordenadores_df = pd.DataFrame({'RAM':[16, 8, 12],
                               'Nucleos_procesador':[8, 4, 8],
                               'Horas_autonomiaa':[8, 12, 7]})


def distancia_manhattan(a, b):
    return sum(abs(a - b))

print("A-B",distancia_manhattan(ordenadores_df.iloc[0], ordenadores_df.iloc[1])) 
print("A-C",distancia_manhattan(ordenadores_df.iloc[0], ordenadores_df.iloc[2])) 
print("B-C",distancia_manhattan(ordenadores_df.iloc[1], ordenadores_df.iloc[2]))