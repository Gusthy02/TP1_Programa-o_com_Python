ano_2_digitos = '02'
tempo_minutos = 150 + int(ano_2_digitos)
tempo_horas = 3.6578

def converte_minutos_para_horas(minutos):
    return round(minutos / 60, 2)

def converte_horas_para_minutos(horas):
    return round(horas * 60, 2)

tempo_minutos_em_horas = converte_minutos_para_horas(tempo_minutos)
tempo_horas_em_minutos = converte_horas_para_minutos(tempo_horas)

print(f'Minustos covnertidos para horas: {tempo_minutos_em_horas}')
print(f'Horas covnertidos para minutos: {tempo_horas_em_minutos}')