# Comando: Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.

#--------------------------------------------------
#            DESCONTO APLICADO EM 5%
#--------------------------------------------------

product = float(input('Informe o valor do produto para consulta de promocao: '))

taxa_desconto = 0.05
valor_desconto = product * taxa_desconto
new_price = product - valor_desconto

print(f'\n O produto ficou custando {new_price:.2f} com os 5% aplicado!!!')