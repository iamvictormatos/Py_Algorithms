#Comando: Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.

#--------------------------------------------------------------
#            EQUACAO DO SEGUNDO GRAU
#--------------------------------------------------------------

a = float(input("Informa o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

Delta = (b**2) - (4 * a * c)
print(f"O valor de delta e de {Delta:.2f}")

if a == 0:
    print("O valor de A nao pode ser 0")
elif Delta < 0:
    print("O valor de Delta nao resulta em valor negativo!!!")
else:
    raiz = Delta ** 0.5

    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)

    print (f"O valor de x1 e {x1:.2f}")
    print (f"O valor de x2 e {x2:.2f}") 