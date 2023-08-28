#listas
l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]

#crear conjuntos a partir de las listas l1 y l2
s1=set(l1)
s2=set(l2)
print("conjunto s1:", s1)
print("conjunto s2:", s2)

#Encontrar los elementos que son comunes a s1 y s2 y almacenarlos en un conjunto s3
tosem=set().union(s1).union(s2)
s3=set(tosem).intersection(s1).intersection(s2)
ss3=set(s3)
print("conjunto s3: Elementos que son comunes a s1 y s2: ", ss3)

#Encontrar los elementos que son únicos para s1 y s2 y almacenarlos en un conjunto s4
val12= s1.difference(s2)
val21= s2.difference(s1)
s4= val12.union(val21)
ss4=set(s4)
print("elementos que son únicos para s1 y s2", ss4)


#Crear una nueva lista l3 que contenga los elementos de s3 y s4 ordenados por el número entero de cada tupla
ml3=list(s3)
ml4=list(s4)
l3=ml3 + ml4

l3.sort(key=lambda x: x[1])

print("Elementos de s3 y s4 ordenados por el número entero de cada tupla", l3)
