print('___Sobre: Calcula Reajuste Salarial___\n')

salario = float(input('Digite o salário atual: '))
aumento = float(input('Por exemplo, para 15% de aumento, digite apenas o número 15\nDigite o valor(apenas números) do aumento: '))
taxa = (100+aumento)/100
salario_final = salario*taxa

print(f'O salário final é: R$ {salario_final:.2f} reais')