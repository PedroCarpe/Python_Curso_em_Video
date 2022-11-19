#Curso em Vídeo: Curso de Python, ex03

n1,n2 = input('Digite um número: ').split())
n1 = int(n1)
n2 = int(n2)
print(f'A soma entre {n1} e {n2} é: {n1+n2}')

#Outra possibilidade
n1,n2 = map(int,input('Digite um número: ').split())
print(f'A soma entre {n1} e {n2} é: {n1+n2}')

#Outra possibilidade
n1,n2 = map(int,input('Digite um número: ').split())
soma = n1+n2
print('A soma entre {} e {} é igual a: {}'.format(n1,n2,soma))
