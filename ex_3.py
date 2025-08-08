km_por_dia = 19
ano_2_digitos = '25'
gasto_diario = km_por_dia + int(ano_2_digitos)

print(f'Total em uma semana: {km_por_dia * 7}')
print(f'Diferença entre 100 reais e o gasto diário: {100 - gasto_diario}')
print(f'Quantos dias o valor de R$500 cobre: {500 // gasto_diario}')
print(f'Porcentagem do gasto diário em relação a 100: {gasto_diario % 100}')
print(f'Média diária de custo por km: {gasto_diario / km_por_dia}')