print('___Procurando uma String___')

nome = input('\nDigite seu nome completo: ')

nome = nome.lower().strip().split()
valor_boleano = 'silva' in nome

print(valor_boleano)