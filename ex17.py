import math
print('___Sobre: Calculo da Hipotenusa de um Triangulo Retangulo___\n')

cateto_oposto = float(input('Valor do cateto oposto: '))
cateto_adj = float(input('Valor do cateto adjacente: '))
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adj**2) 

print(f'O valor da hipotenusa é : {hipotenusa:.3f}')