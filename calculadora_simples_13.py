import operator


def calculadora_simples(numero1: int, numero2: int, operador: str):
    if operador == '+':
        print(numero1 + numero2)
        return numero1 + numero2
    elif operador == '-':
        print(numero1 - numero2)
        return numero1 - numero2
    elif operador == '*':
        print(numero1 * numero2)
        return numero1 * numero2
    elif operador == '/':
        print(numero1 / numero2)
        return numero1 / numero2


calculadora_simples(12, 12, '+')

n1 = 3
n2 = 3
o = "*"
print(f'{n1} {o.matmul()} {n2}')
print(dir("+"))
