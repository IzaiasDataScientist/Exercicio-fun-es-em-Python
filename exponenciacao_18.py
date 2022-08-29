def exponenciacao(num1: float, num2: float):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError as e:
        print(e)
        return False
    return num1**num2


exponenciacao("es", 3)
exponenciacao(3, "asd")
print(exponenciacao(2, 3))
