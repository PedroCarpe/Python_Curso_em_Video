print('___Cálculo de Tabuada___')

n = int(input('Digite um número para a tabuada: '))
cont = 1

while cont <= 10:
    if cont != 10:
        print(f'{n}  X  {cont} = {cont * n}')
    else:
        print(f'{n}  X {cont} = {cont * n}')
    cont += 1