print('___Sobre: Aluguel de Carro___\n')

dias = int(input('Por quantos dias o carro foi alugado? '))
distancia = float(input('Quantos Kilometros foram rodados? '))

valor_total = dias*60+distancia*0.15
print(f'O valor total a ser pago é de: R$ {valor_total:.2f} reais.')