def maior_menor():
    num1: int = input('Entre com o primeiro numero')
    num2: int = input('Entre com o segundo numero')

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Insira um numero inteiro positivo.")
        return -1
    return print(max([num1, num2]))


maior_menor()

"""if num1 > num2:
        print(f'O {num1} eh o maior numero.')
    elif num2 > num1:
        print(f'O {num2} eh o maoir numero.')
    else:
        print('Os numeros são iguais')"""