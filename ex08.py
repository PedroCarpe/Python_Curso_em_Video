import math

print('___Sobre: Conversão de medidas de comprimento___\n')
print('Unidades disponíveis: km hm dam m dm cm mm')
unidade1,unidade2 = input('\nDigite as unidades a serem convertidas, respectivamente: ').split()
valor = float(input('Digite o valor a ser convertido: '))

unidades = ['km','hm','dam','m','dm','cm','mm']
for x in range(len(unidades)):
    if (unidade1) == unidades[x]:
        a = x
    if (unidade2) == unidades[x]:
        b = x

c = math.fabs(a-b)
if (a-b) < 0:
    print(f'\nResposta: {valor:.2f}{unidade1} equivale a {valor*math.pow(10,c):.2f}{unidade2}')

if (a-b) > 0:
    print(f'\nResposta: {valor:.2f}{unidade1} equivale a {valor*(1/math.pow(10,c)):.2f}{unidade2}')