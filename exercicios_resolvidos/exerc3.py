# Comando: Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.

name = input('Nome do funcionario: ')
mes = input('Selecione o mes de interesse: ')
sal = float(input('Salario: '))

print(f'\nO funcionario(a) {name} tem um salario de R${sal} em {mes}.')