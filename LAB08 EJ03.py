#Generador de contarseñas
import random
import string

def gen_contraseña():
    try:
        longitud=int(input('Ingrese longitud: '))

        if longitud < 8:
            print('La longitud debe ser mayor de 8 caracteres en adelante!')
            gen_contraseña()

        caract= string.ascii_letters + string.digits + string.punctuation
        contraseña=''.join(random.choice(caract) for i in range(longitud))
        print(contraseña)
    except ValueError:
        print('Valor no admitible!')
        gen_contraseña()
gen_contraseña()