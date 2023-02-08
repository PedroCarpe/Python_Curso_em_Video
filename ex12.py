print('___Sobre: Calcula Desconto no Preço de um Produto___\n')

preco = float(input('Digite o preço do produto: '))
desconto = float(input('Por exemplo, para 5% de desconto, digite apenas o número 5\nDigite o valor(apenas números) do desconto: '))
taxa = (100-desconto)/100
preco_final = preco*taxa

print(f'O preço final do produto é: R$ {preco_final:.2f} reais')