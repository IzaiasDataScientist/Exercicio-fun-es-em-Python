import math


def volume_cilindro(raio, altura):
    V = math.pi * raio**2 * altura
    print(f'O volume do cilindro é {V}')


volume_cilindro(4, 9)
