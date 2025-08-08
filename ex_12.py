from math import pi

desconto_txte = '19'
valor_produto = 599.99
desconto_num = int(desconto_txte) / round(pi, 2)

def calcula_desconto(desconto, valor_produto):
    valor_desconto = (desconto / 100) * valor_produto
    return valor_produto - valor_desconto
    
valor_final = calcula_desconto(desconto_num, valor_produto)

print(f'Valor final: {valor_final:.2f}')