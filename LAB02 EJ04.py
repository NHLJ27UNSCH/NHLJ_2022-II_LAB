def espacio():
    for i in range(20):
            print(' ')

def promo_3000():
    try:
        cant_prom=3000

        precio_total=int(input('Precio total de compras: '))
        if precio_total>3000:
            total_a_pagar=precio_total*0.9
            print(f'El precio final de la compra es: {total_a_pagar}')
        elif precio_total<3000:
            total_a_pagar=precio_total*0.95
            print(f'El precio final de la compra es: {total_a_pagar}')
        else:
            espacio()
            print('Error!')

        bucle='a'
        while bucle !='0':
            bucle=input('Determinar otra precio final?\n1. Si\n2. No\n')
            if bucle=='1':
                espacio()
                promo_3000()

            elif bucle=='2':
                espacio()
                print('Programa finalizado!')
                quit()

            else:
                espacio()
                print('Error!')



    except ValueError:
        espacio()
        print('Error!')
        promo_3000()

promo_3000()