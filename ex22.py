print('___Sobre: Analisador de Nomes___\n')

nome = input('Digite seu nome completo: ')

print('\nSeu nome em maiúsculas, é: '+nome.upper())
print('Seu nome em maiúsculas, é: '+nome.lower())

espaços = nome.count(" ")
primeiroNome = nome.split()

print(f'Seu nome tem ao todo {len(nome)-espaços} letras')
print(f'Seu 1º nome é {primeiroNome[0]} e tem {len(primeiroNome[0])} letras')