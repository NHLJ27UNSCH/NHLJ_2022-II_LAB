# Encontrar la factorial de un número
factorial=1
num=int(input("ingrese numero: "))
if num==0:
    print('el factorial de 0 es: 1')
elif num>0:
    for i in range(1, num+1):
        factorial=factorial*i
    print("Su factorial es:",factorial)
else:
    print('No existe!')