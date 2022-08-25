def formam_um_triangulo(num1, num2, num3):
    if num1 < (num2 + num3) and num3 < (num1 + num2) and num2 < (num1 + num3):
        return True
    else:
        return False


def tipos_triangulo(num1: int, num2: int, num3: int):
    if formam_um_triangulo(num1, num2, num3):
        if num1 == num2 == num3:
            print("Triangulo equilatero")
            return "Triangulo equilatero"
        elif num1 == num2 or num2 == num3 or num1 == num3:
            print('isosceles')
            return 'Triangulo isosceles'
        elif num1 != num2 != num3:
            print("Triangulo escaleno")
            return "Triangulo escaleno"


tipos_triangulo(23, 23, 23)
formam_um_triangulo(2, 3, 10)
