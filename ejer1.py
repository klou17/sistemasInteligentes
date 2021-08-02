# Por comprensión:

def cuadrados1(l):
    a = [ a*a for a in l ]
    return a

# Usando bucle:

def cuadrados2(l):
    a = []
    for i in l:
        a.append(i*i)
    return a

def vocales_consonantes(s):
    vocales = "AEIOU"
    for i in s:
        if vocales.find(i)==-1:
            print('{0} es consonante'.format(i))
        else:
            print('{0} es vocal'.format(i))

# -----------
# EJERCICIO 3
# -----------

# Usando como técnica principal la definición de secuencias por comprensión,
# definir las siguientes funciones:

# a) Dada una lista de números naturales, la suma de los cuadrados de los
#    números pares de la lista.

# Ejemplo:
# >>> suma_cuadrados([9,4,2,6,8,1])
# 120

def suma_cuadrados(l):
    t=0
    for i in l:
        if i % 2 == 0:
            t += i*i        
    return t

# b) Dada una lista de números l=[a(1),...,a(n)], calcular la sumatoria de i=1
#    hasta n de i*a(i).

# Ejemplo:

# >>> suma_fórmula([2,4,6,8,10])
# 110


def suma_formula(l):
    n = len(l)
    t = 0
    l1 = [(i+1)*l[i] for i in range(n)]
    for k in l1:
        t+=k
    return t

# c) Dadas dos listas numéricas de la misma longitud representando dos puntos
#    n-dimensionales, calcular la distancia euclídea entre ellos. 

# Ejemplo:

# >>> distancia([3,1,2],[1,2,1])
# 2.449489742783178

def sqrt(n):
    return n**(1/2.0)

def distancia(l1,l2):
    n  = len(l1)
    l3 = [(l1[i]-l2[i])**2 for i in range(n)]
    t = 0
    for i in range(n):
        t+=l3[i]
    return sqrt(t)

# d) Dada una lista y una función de un argumento, devolver la lista de los
#    resultados de aplicar la función a cada elelemnto de la lista.

# Ejemplo:

# >>> map_mio(abs,[-2,-3,-4,-1])
# [2, 3, 4, 1]

def map_mio(f,l):
    l1 = [ f(a) for a in l]
    return l1

# e) Dada un par de listas (de la misma longitud) y una función de dos
#    argumentos, devolver la lista de los resultados de aplicar la función a
#    cada par de elementos que ocupan la misma posición en las listas de
#    entrada.


# Ejemplo:

# >>> map2_mio((lambda x,y: x+y) ,[1,2,3,4],[5,2,7,9])
# [6, 4, 10, 13]

def map2_mio(f,l1,l2):
    l3 = [f(l1[i],l2[i]) for i in range(len(l1))]
    return l3

# f) Dada una lista de números, contar el número de elementos que sean múltiplos
#    de tres y distintos de cero. 

# Ejemplo:

# >>> m3_no_nulos([4,0,6,7,0,9,18])
# 3

def m3_no_nulos(l):
    n = len(l)
    l1 = [ 1 for i in range(n) if (l[i] % 3 == 0 and l[i] != 0)]
    return sum(l1)
#   return l1.len()

# f) Dadas dos listas de la misma longitud, contar el número de posiciones en
#    las que coinciden los elementos de ambas listas.  

# Ejemplo:

# >>> cuenta_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# 3


def cuenta_coincidentes(l1,l2):
    n = len(l1)
    t = sum([ 1 for i in range(n) if l1[i] == l2[i] ])
    return t

# g) Dadas dos listas de la misma longitud, devolver un diccionario que tiene
# como claves las posiciones  en las que coinciden los elementos de ambas
# listas, y como valor de esas claves, el elemento coincidente. 

# Ejemplos:

# >>> dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# {1: 2, 3: 8, 4: 9}
# >>> dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6])
# {1: 8, 2: 1, 3: 2, 4: 1}

def dic_posiciones_coincidentes(l1,l2):
    n = len(l1)
    l3 = {i:l1[i] for i in range(n) if l1[i]==l2[i]}
    return l3



print (cuadrados1([5,8,1,-3]))
print (cuadrados2([5.8,11,-3]))
print (vocales_consonantes("inteligencia"))