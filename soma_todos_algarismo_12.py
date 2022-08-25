def soma_todos_algarismo(numero):
    soma = sum([int(i) for i in str(numero)])
    print(soma)
    return soma


soma_todos_algarismo(251322)

