# Comando: Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

#--------------------------------------------------
#            CALCULO DE AREA
#--------------------------------------------------

largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))

area = largura * altura
tinta = area / 2

print(f'\n--- Resultado do Cálculo ---')
print(f'Area total a ser pintada: {area:.2f} m²')
print(f'Quantidade de tinta necessaria: {tinta:.2f} litros')