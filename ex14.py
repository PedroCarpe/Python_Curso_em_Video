print('___Sobre: Conversão de Temperatura___\n')
print('Temperaturas Diponíveis: Celsius(C), Fahrenheit(F) e Kelvin(K)\n')

t1,t2 = input('Digite as temperaturas a serem convertidas(C,F ou K): ').split()
valor = float(input('Digite o valor a ser convertido: '))

conversao = 0

if t1=='C' and t2=='F':
    conversao = valor*(9/5)+32
    print(f'{conversao:.2f}')
elif t1=='F' and t2=='C':
    conversao = (valor-32)*(5/9)
    print(f'{conversao}')
elif t1=='C' and t2=='K':
    conversao = valor+273
    print(f'{conversao}')
elif t1=='K' and t2=='C':
    conversao = valor-273
    print(f'{conversao:.2f}')
elif t1=='F' and t2=='K':
    conversao = (valor-32)*(5/9)
    conversao = conversao+273
    print(f'{conversao:.2f}')
elif t1=='K' and t2=='F':
    conversao = valor-273
    conversao = conversao*(9/5)+32
    print(f'{conversao:.2f}')    

