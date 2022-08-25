import math


def quadradoPerfeito(numero: int):
    try:
        if (float(math.sqrt(abs(numero))) - int(math.sqrt(abs(numero)))) == 0.0:
            print(math.sqrt(abs(numero)))
            return f"quadrado perfeito"
        else:
            print(math.sqrt(abs(numero)))
            return f"quadrado imperfeito"
    except TypeError as e:
        print(e)


print(quadradoPerfeito(9))
