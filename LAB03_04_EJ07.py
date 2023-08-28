#Contar caracteres y palabras dada la siguiente frase
frase =  "Estoy aprendiendo Python y me está gustando mucho. ¡Es genial!"

agr = frase.split(' ')  #agrupar cada palabra en una lista

print("Total de caracteres: ",len(frase))
print("Total de palabras: ", len(agr))