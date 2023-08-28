#Generador de Contraseñas
import random
import string

def generar_contraseña(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True):
    try:
        if longitud < 1:
            raise ValueError("La longitud de la contraseña debe ser al menos 1.")
        
        caracteres = ""
        
        if incluir_mayusculas:
            caracteres += string.ascii_uppercase

        if incluir_minusculas:
            caracteres += string.ascii_lowercase

        if incluir_numeros:
            caracteres += string.digits

        if incluir_especiales:
            caracteres += string.punctuation

        if not caracteres:
            raise ValueError("Debes incluir al menos un tipo de carácter en la contraseña.")
        
        generador_caracteres = lambda: random.choice(caracteres)
        contraseña = ''.join(generador_caracteres() for _ in range(longitud))
        return contraseña

    except ValueError as e:
        return str(e)

def generador():
    try:
        longitud = int(input("Longitud de la contraseña: "))
        incluir_mayusculas = input("Incluir mayúsculas (S/N): ").upper() == 'S'
        incluir_minusculas = input("Incluir minúsculas (S/N): ").upper() == 'S'
        incluir_numeros = input("Incluir números (S/N): ").upper() == 'S'
        incluir_especiales = input("Incluir caracteres especiales (S/N): ").upper() == 'S'

        contraseña_generada = generar_contraseña(
            longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales
        )
        
        if "Debes" in contraseña_generada:
            print(contraseña_generada)
        else:
            print("Contraseña generada:", contraseña_generada)

    except ValueError:
        print("Entrada incorrecta!")
        generador()

generador()