#Listas de números
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

#Convertir listas en conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

#Conjunto de números presentes en las tres listas
conjunto_interseccion = conjunto1 & conjunto2 & conjunto3

#Conjunto de números presentes en al menos una de las listas
conjunto_union = conjunto1 | conjunto2 | conjunto3

#Conjunto de números presentes en la primera lista pero no en la última
conjunto_diferencia = conjunto1 - conjunto3

#Convertir conjuntos en tuplas y sumar primer y último elemento de cada tupla
tupla_interseccion = (tuple(conjunto_interseccion),)
tupla_union = (tuple(conjunto_union),)
tupla_diferencia = (tuple(conjunto_diferencia),)

suma_primer_ultimo_interseccion = tupla_interseccion[0][0] + tupla_interseccion[0][-1]
suma_primer_ultimo_union = tupla_union[0][0] + tupla_union[0][-1]
suma_primer_ultimo_diferencia = tupla_diferencia[0][0] + tupla_diferencia[0][-1]


print("Conjunto de intersección:", conjunto_interseccion)
print("Conjunto de unión:", conjunto_union)
print("Conjunto de diferencia:", conjunto_diferencia)

print("Suma del primer y último elemento de la tupla de intersección:", suma_primer_ultimo_interseccion)
print("Suma del primer y último elemento de la tupla de unión:", suma_primer_ultimo_union)
print("Suma del primer y último elemento de la tupla de diferencia:", suma_primer_ultimo_diferencia)
