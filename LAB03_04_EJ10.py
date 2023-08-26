palabra=input('Palabra o frase: ')
spalabra = palabra.casefold()
revpalabra = reversed(spalabra)
if list(revpalabra)==list(spalabra):
    print('palindromo!')
else:
    print('no es palindromo')