# Comando: Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.

number = int(input("Digite um numero: "))
ant = number - 1
suc = number + 1

print(f"\nO antecessor de {number} e {ant}")
print(f"O sucessor de {number} e {suc}")