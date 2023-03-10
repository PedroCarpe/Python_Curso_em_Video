print('___Sobre: Analisador de Nomes___\n')

nome = input('Digite seu nome completo: ')

print('\nSeu nome em maiúsculas, é: '+nome.upper())
print('Seu nome em minúsculas, é: '+nome.lower())

espaços = nome.count(" ")
primeiro_nome = nome.split()

print(f'Seu nome tem ao todo {len(nome)-espaços} letras')
print(f'Seu 1º nome é {primeiro_nome[0]} e tem {len(primeiro_nome[0])} letras')
