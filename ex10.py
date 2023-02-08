import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
r = requisicao.json()
dic = r['USDBRL']
dolar = float(dic['bid'])

print('___Sobre: Conversor de Moedas___\n')
print(f'Cotação de Hoje, 1 dolar equivale a: R$: {dolar} reais\n')

print('Para converter de "Real-Dolar", digite 1\nPara converter de "Dolar-Real", digite 2')
moeda = input('Entrada: ')
qtd = float(input('Digite a quantidade a ser convertida: '))

if moeda == '1':
    print('\nReal-Dolar')
    print(f'{qtd} reais equivale a {qtd/dolar:.2f} dolares')      
elif moeda == '2':
    print('\nDolar-Real')
    print(f'{qtd} dolares equivale a {qtd*dolar:.2f} reais')