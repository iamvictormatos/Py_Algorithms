#Comando: Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.

import math

#--------------------------------------------------------------
#            EQUACAO DO SEGUNDO GRAU
#--------------------------------------------------------------

A = float(input("Informa o valor de A: "))
B = float(input("Informe o valor de B: "))
C = float(input("Informe o valor de C: "))

Delta = (B**2) - (4 * A * C)
print(f"O valor de delta e de {Delta:.2f}")

X = -B +- raiz Delta