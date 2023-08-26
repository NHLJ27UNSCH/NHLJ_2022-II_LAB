#E8
frase = "Aprendiendo Python con Edem"

sep = frase.split(' ')          #Enlistar cada palabra
sep.reverse()                   #Inversion de cada elemento

inv_frase = ' '.join(sep)       #Unir de elementos de la lista con espacios
print(inv_frase)