# Comando: Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
m = (nota1 + nota2) / 2

print(f'\nA media entre {nota1:.1f} e {nota2:.1f} e igual a {m:.1f}')