#calcular serie de fibonacchi hasta numero n
def fibonacci():
    n=int(input('Ingrese rango de serie: '))
    a = 0
    b = 1

    for k in range(n):
        c = b+a
        a = b
        b = c
        print(a)
fibonacci()