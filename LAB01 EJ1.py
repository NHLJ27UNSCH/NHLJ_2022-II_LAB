#Determinar si un número es primo
def num_primo():
    try:
        num=int(input("numero a determinar: "))
        if num==1:
            print('1 no es numero primo')
        elif num==0:
            print('0 no es un numero primo')
        
        elif num>1:
            for i in range(2, num):
                if (num%i)==0: #se halla el resto de dividir el numero desde 2 hasta el mismo numero para encontrar factores
                    print('no es primo')
                    break
                else:
                    print('es primo!')
        else:
            print('error!')
    except ValueError:
        print('Error de valor!')
        num_primo()

num_primo()
