#Calculadora simple de dos numeros

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def calcular():
    try:
        N1 = float(input("Ingresa primer número: "))
        N2 = float(input("Ingresa segundo número: "))
        operacion = input("Seleccione operación:\n1. sumar\n2. restar\n3. multiplicar\n4. dividir\n")

        if operacion == '1':
            resultado = suma(N1, N2)
            print(f"Resultado: {N1} + {N2} = {resultado:.2f}")
        elif operacion == '2':
            resultado = resta(N1, N2)
            print(f"Resultado: {N1} - {N2} = {resultado:.2f}")
        elif operacion == '3':
            resultado = multiplicacion(N1, N2)
            print(f"Resultado: {N1} * {N2} = {resultado:.2f}")
        elif operacion == '4':
            resultado = division(N1, N2)
            print(f"Resultado: {N1} / {N2} = {resultado:.2f}")
        else:
            print("Seleccion invalida!")
            return

    except ValueError:
        print("Entrada incorrecta")
        calcular()

    except ZeroDivisionError as e:
        print(str(e))
        calcular()


calcular()
