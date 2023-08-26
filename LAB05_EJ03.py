#tres listas de numeros enteros
li1=list(range(1,11))
li2=list(range(5,16))
li3=list(range(10,21))

print("lista 1:", li1)
print("lista 2:", li2)
print("lista 3:", li3)


#convertir listas a conjuntos
sli1= set(li1)
sli2= set(li2)
sli3= set(li3)
print("conjunto 1:", sli1)
print("conjunto 2:", sli2)
print("conjunto 3:", sli3)


#Conjunto de todos los números que están presentes en las tres listas
tot3=set().union(sli1).union(sli2).union(sli3)
rep3=set(tot3).intersection(sli1).intersection(sli2).intersection(sli3)
print("Conjunto de numeros presentes en las tres listas", rep3)

#Conjunto de todos los números que están presentes en al menos una de las listas
#alme1=sli1.intersection(sli2)
#print("Conjunto de numeros presentes en al menos una de las listas", alme1)

#Conjunto de todos los números que están presentes en la primera lista, pero no en la última
tnp=sli1.difference(sli3)
print("Conjunto de numeros presentes en la primera lista, pero no en la última", tnp)

#Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla.
tli1= tuple(sli1)
tli2= tuple(sli2)
tli3= tuple(sli3)
print(tli1)

sumdt1= tli1[0] + tli1[10]
print(sumdt1)
sumdt2= tli2[0] + tli2[10]
print(sumdt2)
sumdt3= tli3[0] + tli3[10]
print(sumdt3)