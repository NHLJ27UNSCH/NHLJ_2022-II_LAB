#Encontrar todos los numeros primos menores que n

n = int(input("Ingrese numero: "))

num_primos = []
for i in range(2, n-1):
    sera_primo = True
    for j in range(2, int(i/2)+1):
        if (i % j) == 0:
            sera_primo = False
    if sera_primo:
        num_primos += [i]

print(num_primos)