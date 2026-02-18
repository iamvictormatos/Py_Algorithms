# Comando: Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.

number = float(input("Digite um numero: "))
dobro = number * 2
ter = number / 3 #number * (1/3)

print(f"\nO dobro de {number:.1f} e {dobro:.1f}")
print(f"A terca parte de {number:.1f} e {ter:.5f}")