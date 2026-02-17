#Comando: Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

#--------------------------------------------------------------
#            CONVERSAO DE DOLAR
#--------------------------------------------------------------

money = float(input("Qual valor disponivel em sua carteira?: "))
dolar = money / 3.45

print(f"Voce pode comprar Us${dolar} com R${money}!")