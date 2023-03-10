print('___Sobre: Notação Numérica Posicional___')

while True:
    numero = int(input('\nInforme um número entre 0-9999: '))
    if 0 <= numero <= 9999:
        break
    else:
        print('Número fora do intervalo, digite novamente!')


numero = str(numero)

numero = list(numero)

sistema_de_numeracao = [' unidade(s) de milhar',' centena(s)',' dezena(s)',' unidade(s)']
print('O número informado possui:')

for contador in range(len(numero)):
    if len(numero) == 4:
        print(numero[contador]+sistema_de_numeracao[contador])
    if len(numero) == 3:
        print(numero[contador]+sistema_de_numeracao[contador+1])
    if len(numero) == 2:
        print(numero[contador]+sistema_de_numeracao[contador+2])
    if len(numero) == 1:
        print(numero[contador]+sistema_de_numeracao[-1])
        