#Cifrado Cesar

def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            mayuscula = letra.isupper()
            letra = letra.lower()
            codigo = ord(letra)
            codigo_desplazado = (codigo - 97 + desplazamiento) % 26 + 97
            if mayuscula:
                resultado += chr(codigo_desplazado).upper()
            else:
                resultado += chr(codigo_desplazado)
        else:
            resultado += letra
    return resultado

def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)

texto_original = input('Ingrese texto: ')
desplazamiento = int(input('Ingrese desplazamiento: '))

texto_cifrado = cifrar_cesar(texto_original, desplazamiento)
print("Texto cifrado:", texto_cifrado)

texto_descifrado = descifrar_cesar(texto_cifrado, desplazamiento)
print("Texto descifrado:", texto_descifrado)