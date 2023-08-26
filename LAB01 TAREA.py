#Pida al usuario que introduzca 5 números.
#Guarde esos números en una lista.
lst=list()
for i in range(5):
    val=int(input('Inserte numero: '))
    lst.append(val)
print(lst)

#Calcule y muestre la media de esos números.
media=sum(lst)/len(lst)
print(media)