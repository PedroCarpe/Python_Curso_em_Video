print('___Sobre: Parte Inteira/Decimal de um Numero___\n')

num = input('Digite um numero: ')
numero = float(num)
parte_inteira = int(numero)
parte_decimal = numero-int(numero)
posicao = -1

'''a ideia deste trecho é: calcular o numero de casas decimais do numero,
para utilizar no print formatado'''
if num.find('.') != -1:
    posicao = num.find('.')
    qtd_casas_decimais = (len(str(numero))-(posicao+1))
    

if posicao != -1:
    print(f'Parte inteira: {parte_inteira}')
    print(f'Parte decimal: {parte_decimal:.{qtd_casas_decimais}f}')
else:
    print(f'Parte inteira: {parte_inteira}')
    print(f'Parte decimal: {parte_decimal}')