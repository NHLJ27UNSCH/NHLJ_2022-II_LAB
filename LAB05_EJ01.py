edades=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


#ordenar lista y encontrar edad min y max
edades.sort()
minval=min(edades)
maxval=max(edades)

print("lista ordenada: ", edades)
print("Valor minimo: ", minval)
print("Valor maximo: ", maxval)


#Agregar de nuevo la edad min y max a la lista
edades.append(maxval)
edades.append(minval)

print("lista ordenada con valores minimos y maximo agregadas: ", edades)


#Edad mediana (un elemento del medio o dos elementos del medio divididos por dos)
canted=len(edades)
elemed=int(canted/2)
edamed=(edades[elemed])/2

print("cantidad de valores: ", canted)
print("posicion del elemento del medio: ", elemed)
print("edad mediana:", edamed)


#Edad promedio (suma de todos los elementos divididos por su número)
promed=sum(edades)/canted
print("promedio de edades:", promed)


#Rango de edades (máximo menos mínimo)
Raned=maxval-minval
print("rango de edades:", Raned)

#Comparar min-prom y max-prom mediante abs()
comp_min=abs(minval-promed)
comp_max=abs(maxval-promed)

if comp_min < comp_max:
    print("La diferencia mínima al promedio es menor.")
elif comp_min > comp_max:
    print("La diferencia máxima al promedio es menor.")
else:
    print("Las diferencias son iguales.")