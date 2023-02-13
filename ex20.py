from random import shuffle

print('___Sobre: Sorteando os Items da Lista___\n')

alunos = []
cont = 1
qtd_alunos = int(input('Digite a quantidade de alunos, para a lista: '))

while cont <= qtd_alunos:
    alunos.append(input('Digite o nome do alunoª: '))
    cont += 1

shuffle(alunos)
print(f'\nA ordem de apresentação será: {alunos}')    