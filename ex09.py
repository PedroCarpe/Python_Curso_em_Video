print('___Sobre: Tabuada___\n')

num = int(input('Digite um numero, para a tabuada: '))

for x in range(11):
    if x >= 1:
        print(f'{num}  x {x:2} = {num*x}')