print('___Sobre:Calcula Quantidade de Tinta para Pintura de Parede___')
print('Dado que, 1L de tinta, cobre 2m² de área\n')

comprimento = float(input('Digite o comprimento da parede: '))
altura = float(input('Digite a altura da parede: '))

qtd_d_tinta = (comprimento*altura)/2

print(f'A quantidade de tinta(L) para pintar a parede é de: {qtd_d_tinta:.2f}L')