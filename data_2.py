
data = "19/12/2000"
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

def find_data(data):
    return f'{int(data[:2])} de {meses[(int(data[3:5])) - 1]} de {data[6:]}'


print(find_data(data))
