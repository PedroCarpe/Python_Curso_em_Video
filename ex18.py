from math import sin,cos,tan,radians

print('___Sobre: Calculo do Seno, Cosseno e Tangente de um Angulo___\n')

angulo = float(input('Digite o valor de um angulo: '))
radiano = radians(angulo)

seno = sin(radiano)
coseno = cos(radiano)
tangente = tan(radiano)

print(f'Seno({angulo}º): {seno:.2f} \nCosseno({angulo}º): {coseno:.2f} \nTangente({angulo}º): {tangente:.2f}')