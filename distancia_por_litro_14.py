def distancia_por_litro(distancia: float, litros: float):
    consumo: float = distancia/litros
    if consumo < 8:
        print('Venda o carro!')
        return 'Venda o carro!'
    elif 8 < consumo < 14:
        print('Economico!')
        return 'Economico!'
    elif consumo >= 14:
        print('Super economico!')
        return 'Super economico!'


distancia_por_litro(350, 50)
distancia_por_litro(500, 50)
distancia_por_litro(750, 50)
