#determinar la edad de postulantes, pero cuando se les realiza la entrevista sólo se les pregunta el año en que nacieron.

def espacio():
    for i in range(20):
            print(' ')

def edad_del_postulante():
    try:
        año_de_nacimiento=int(input('Ingrese año de nacimiento del postulante: '))
        año_actual=2023
        edad=año_actual-año_de_nacimiento
        espacio()


        print(f'Edad del postulante: {edad}')
        bucle=input('Determinar otra edad?\n1. Si\n2. No\n')
        if bucle=='1':
            espacio()
            edad_del_postulante()


        elif bucle=='2':
            espacio()
            print('Programa finalizado!')
            quit()
        else:
            print('Error!')

    except ValueError:
        print("Error!")
        edad_del_postulante()
edad_del_postulante()