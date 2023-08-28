#Convertir Celsius a fahrenheit

def fah_a_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

def cel_a_fah(celsius):
    return celsius * 9/5 + 32
def convertir():
    try:
        temperatura=float(input('Ingrese temperatura: '))
        unidad=input('Ingrese unidad (C / F): ').upper()

        if unidad == 'C':
            conversion=cel_a_fah(temperatura)
            print(f'{temperatura}°C equivale a {conversion}°F')
        elif unidad=='F':
            conversion=fah_a_cel(temperatura)
            print(f'{temperatura}°F equivale a {conversion}°C')
        else:
            print('Unidad no valida, ingrese de nuevo!')
            convertir()
    except ValueError:
        print('Valor no admitible!')
        convertir()

convertir()