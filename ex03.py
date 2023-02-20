print('___Sobre: Operação de Soma___\n')
n1,n2 = input('Digite um número: ').split()
n1 = float(n1)
n2 = float(n2)
print(f'A soma entre {n1} e {n2} é: {n1+n2}')

#Outra possibilidade
n1,n2 = map(float,input('Digite um número: ').split())
print(f'A soma entre {n1} e {n2} é: {n1+n2}')

#Outra possibilidade
n1,n2 = map(float,input('Digite um número: ').split())
soma = n1+n2
print('A soma entre {} e {} é igual a: {}'.format(n1,n2,soma))
