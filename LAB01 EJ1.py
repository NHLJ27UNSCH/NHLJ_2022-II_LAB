#Determinar si un número es primo
num=int(input("numero a determinar: "))

if num==1:
    print('1 no es primo')
elif num>1:
    for i in range(2, num):
        if (num%i)==0: #se halla el resto de dividir el numero desde 2 hasta el mismo numero para encontrar factores
            print('no es primo')
            break
        else:
            print('es primo!')