persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True,
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}


def espacio():
    for i in range(20):
            print(' ')


#Comprobar si tiene clave habilidades e imprimir la habilidad del medio en la lista de habilidades
def ver_skills_1():
    comprobacion_habilidad='skills' in persona
    if comprobacion_habilidad==True:
        espacio()
        print('Clave encontrada!')
        print('Imprimiendo habilidad del medio en la lista de habilidades...')

        cant_habilidades=len(persona['skills'])
        habilidades=persona['skills']
        valor_medio=int(cant_habilidades/2)
        
        if cant_habilidades % 2 != 0:
            print(f'La habilidad del medio es {habilidades[valor_medio]}')
        
        else:
            print('La cantidad de habilidades es par! Tomando 2 valores')
            print(f'Valores: {habilidades[valor_medio]} y {habilidades[valor_medio-1]}')
    else:
        print('Clave inexistente!')


#Comprobar si tiene clave habilidades, si tiene 'python' en habilidades e imprimir el resultado
def ver_skills_2():
    comprobar_habilidad='skills' in persona
    if comprobar_habilidad==True:
        espacio()
        print('Clave encontrada!')
        print("Buscando 'Python' en habilidades...")
        if 'Python' in persona['skills']:
            print('Python se encuentra en la clave habilidades!!')
        else:
            print('Valor no encontrado')
    else:
        print('Valor inexistente!')
        


#imprimir Frontend, Backend,fullstack o desconocido si la persona posee dichos requisitos
def check_persona():
    if all(valor in persona['skills'] for valor in ('JavaScript', 'React')):
        print("Desarrollador frontend!")

    elif all(valor in persona['skills'] for valor in ('Node', 'Python', 'MongoDB')):
        print("Desarrollador backend!")

    elif all(valor in persona['skills'] for valor in ('React','Node','MongoDB')):
        print("Desarrollador backend!")
        
    else:
        print("Titulo Desconocido")


ver_skills_1()
ver_skills_2()
check_persona()