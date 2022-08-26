def soma(numero1: int, numero2: int):
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
    except ValueError as e:
        print(e)
        return -1

    if numero1 > 0 and numero2 > 0:
        print(numero1 + numero2)
        return numero1 + numero2
    else:
        print('Entre com os numeros positivo.')
        return -1


soma('w', 3)
soma(-1, 3)
soma(3, 6)
soma(3, 6)
