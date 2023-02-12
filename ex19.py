import random

print('___Sobre: Sorteando um Item na Lista___\n')

alunos = []
cont = 1
qtd_alunos = int(input('Digite a quantidade de alunos, para a lista: '))

while cont <= qtd_alunos:
    alunos.append(input('Digite o nome do alunoª: '))
    cont += 1

aluno = random.choice(alunos)
print(f'\nO alunoª escolhido foi: {aluno}')    