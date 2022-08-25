import statistics


def medias(numero1: int, numero2: int, numero3: int, letra: str):
    if letra == "A":
        print("media aritmetica", statistics.mean([numero1, numero2, numero3]))
    elif letra == "P":
        print("media ponderada", int(((numero1*5)+(numero2*3)+(numero3*2))/(5+3+2)))
    else:
        print("Invalid")


var: str = input("A para media aritmetica, e P para media ponderada")

medias(10, 20, 30, var)
